from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from products.models import Product
from .models import StockMovement

# Now we test the real heart of the system:

# 👉 Stock logic
# This is more important than CRUD.

# Create your tests here.
class StockLogicTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="jay", password="pass123")

        self.product = Product.objects.create(
            name="Coke",
            description="Drink",
            category="Beverage",
            quantity_in_stock=5,
            price=20,
            owner=self.user
        )

        self.client.login(username="jay", password="pass123")

    def test_cannot_remove_more_than_available_stock(self):
        url = reverse('stock-movement-create')

        data = {
            "product": self.product.id,
            "movement_type": "OUT",
            "quantity": 10
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.get(id=self.product.id).quantity_in_stock, 5)



    def test_stock_increases_correctly(self):
        url = reverse('stock-movement-create')

        data = {
            "product": self.product.id,
            "movement_type": "IN",
            "quantity": 5
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.product.refresh_from_db()
        self.assertEqual(self.product.quantity_in_stock, 10)