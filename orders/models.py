from django.db import models
from books.models import Book
from users.models import Manager, Customer, User


class BookState(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_price = models.FloatField()
    book_quantity = models.PositiveIntegerField()
    sold_copy_number = models.IntegerField(default=0)

    def __str__(self):
        return self.book_id.book_title


class OrderStatus(models.Model):
    values = [('NEW', 'new'), ('CONFIRMED', 'confirmed'), ('CANCELLED', 'cancelled'), ('COMPLETED', 'completed'),
              ('ILLEGIBLE', 'illegible')]
    status_value = models.CharField(max_length=200, choices=values, default='NEW')

    def __str__(self):
        return self.status_value


class CustomerOrder(models.Model):
    order_date = models.DateField(auto_now_add=True)
    order_status = models.ForeignKey(OrderStatus, default=1, on_delete=models.RESTRICT)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='created_by', null=True)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, related_name='customer', null=True)
    ordered_books = models.ManyToManyField(Book)
    full_price = models.FloatField(default=1.0)

    def __str__(self):
        return self.pk
