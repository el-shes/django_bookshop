from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        CUSTOMER = "CUSTOMER", 'Customer'
        MANAGER = "MANAGER", 'Manager'

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)


class CustomerManager(BaseUserManager):
    """
    Queryset manager for filtering all customers
    """
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CUSTOMER)


class Customer(User):
    base_role = User.Role.CUSTOMER
    customer = CustomerManager()

    class Meta:
        # proxy means that table won't be generated,
        # but we can work with customer data through this table
        proxy = True

    def welcome(self):
        return "Only for Customers"


class ManagerManager(BaseUserManager):
    """
    Queryset manager for filtering all managers
    """
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.MANAGER)


class Manager(User):
    base_role = User.Role.MANAGER

    manager = ManagerManager()

    class Meta:
        # proxy means that table won't be generated,
        # but we can work with customer data through this table
        proxy = True

    def welcome(self):
        return "Only for Managers"
