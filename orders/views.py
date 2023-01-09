from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView
from .models import BookState

from orders.models import CustomerOrder


def count_total_price(list_of_prices):
    return sum(list_of_prices)


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
        return object_list


class DetailOrder(DetailView):
    model = CustomerOrder
    template_name = 'orders/order_details.html'


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


def update_order_status(request, *args, **kwargs):
    CustomerOrder.objects.filter(pk=kwargs['pk']).update(order_status_id=kwargs['order_status_id'])
    customerorder = CustomerOrder.objects.get(pk=kwargs['pk'])
    return render(request, 'orders/order_details.html', {'customerorder': customerorder})
