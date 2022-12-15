from django.contrib import admin
from orders.models import BookState, OrderStatus, CustomerOrder

admin.site.register(OrderStatus)
admin.site.register(BookState)
admin.site.register(CustomerOrder)
