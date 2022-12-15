from django.shortcuts import render

from django.views.generic import ListView, CreateView

from orders.models import CustomerOrder


class OrdersView(ListView):
    model = CustomerOrder
    template_name = 'orders/order_list.html'


class CreateOrder(CreateView):
    model = CustomerOrder
    template_name = 'orders/create_order.html'
    fields = ['customer', 'ordered_books']
