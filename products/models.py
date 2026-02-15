from django.db import models
from django.contrib.auth.models import User
from suppliers.models import Supplier

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    quantity_in_stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name