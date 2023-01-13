from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView
from .models import BookState, OrderStatus

from orders.models import CustomerOrder

CONFIRM_ORDER_STATUS_ID = 2
CANCEL_ORDER_STATUS_ID = 3


def count_total_price(list_of_prices):
    return sum(list_of_prices)


def update_order_status(request, *args, **kwargs):
    """
    when confirming order - validate quantity of books to order, update quantity and assign confirm status
    if not valid - assign status ILLEGIBLE
    when order status is changed to cancel - book_quantity is added back up
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    ordered_books_id_set = CustomerOrder.objects.get(pk=kwargs['pk']).ordered_books.values_list('id', flat=True)
    order_status_id = kwargs['order_status_id']
    if order_status_id == CONFIRM_ORDER_STATUS_ID:
        if validate_confirm_book_quantity(ordered_books_id_set):
            update_book_quantity(ordered_books_id_set, order_status_id)
        else:
            order_status_id = OrderStatus.objects.get(status_value='ILLEGIBLE').pk
    elif order_status_id == CANCEL_ORDER_STATUS_ID:
        update_book_quantity(ordered_books_id_set, order_status_id)
    CustomerOrder.objects.filter(pk=kwargs['pk']).update(order_status_id=order_status_id)
    customerorder = CustomerOrder.objects.get(pk=kwargs['pk'])
    return render(request, 'orders/order_details.html', {'customerorder': customerorder})


def validate_confirm_book_quantity(book_set):
    for book in book_set:
        if BookState.objects.get(book_id=book).book_quantity == 0:
            return False
    return True


def update_book_quantity(book_set, order_status_id):
    for book in book_set:
        book_quantity = BookState.objects.get(book_id=book).book_quantity
        if order_status_id == CONFIRM_ORDER_STATUS_ID:
            BookState.objects.filter(book_id=book).update(book_quantity=book_quantity - 1)
        elif order_status_id == CANCEL_ORDER_STATUS_ID:
            BookState.objects.filter(book_id=book).update(book_quantity=book_quantity + 1)


class OrdersView(ListView):
    model = CustomerOrder
    template_name = 'orders/order_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(Q(customer__first_name__icontains=query) |
                                                    Q(customer__last_name__icontains=query))
        else:
            object_list = self.model.objects.all()

        marked_status = self.request.GET.getlist('order_status')
        if marked_status:
            object_list = self.model.objects.filter(Q(order_status__status_value__in=marked_status))
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrdersView, self).get_context_data(**kwargs)
        context['order_statuses'] = OrderStatus.objects.all()
        return context


class DetailOrder(DetailView):
    model = CustomerOrder
    template_name = 'orders/order_details.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DetailOrder, self).get_context_data(**kwargs)
        context['book_quantity'] = BookState.objects.all()
        return context


class CreateOrder(CreateView):
    model = CustomerOrder
    template_name = 'orders/create_order.html'
    fields = ['customer', 'ordered_books']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        list_ordered_books_id = self.get_form()["ordered_books"].value()
        list_ordered_prices = []
        for book_id in list_ordered_books_id:
            list_ordered_prices.append(BookState.objects.get(book_id=book_id).book_price)
        form.instance.full_price = count_total_price(list_ordered_prices)
        super(CreateOrder, self).form_valid(form)
        return HttpResponseRedirect(self.get_success_url())
