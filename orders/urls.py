from django.urls import path, reverse_lazy
from . import views

app_name = 'orders'

urlpatterns = [
    path('all', views.OrdersView.as_view(), name='all_orders'),
    path('create_order/new', views.CreateOrderAdmin.as_view(success_url=reverse_lazy('orders:all_orders')), name='new_order'),
    path('all/<int:pk>/details', views.DetailOrder.as_view(), name='order_details'),
    path('all/<int:pk>/<int:order_status_id>', views.update_order_status, name='update_order_status'),

    path('create_order/<int:user_id>/new', views.CreateOrderCustomer.as_view(success_url=reverse_lazy('orders:all_orders')), name='new_customer_order')

]
