from django.urls import path, reverse_lazy
from . import views

app_name = 'orders'

urlpatterns = [
    path('all', views.OrdersView.as_view(), name='all_orders'),
    path('create_order/new', views.CreateOrder.as_view(success_url=reverse_lazy('orders:all_orders')), name='new_order'),

]
