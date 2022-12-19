from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView

from orders.models import CustomerOrder


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


class CreateOrder(CreateView):
    model = CustomerOrder
    template_name = 'orders/create_order.html'
    fields = ['customer', 'ordered_books']


class DetailOrder(DetailView):
    model = CustomerOrder
    template_name = 'orders/order_details.html'
