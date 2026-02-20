from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Product

# Create your tests here.

# First target:
# 👉 Test Product ownership isolation

# Meaning:
# User A cannot see User B products.
# User A only sees their own.

class ProductOwnershipTest(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username="jay", password="pass123")
        self.user2 = User.objects.create_user(username="thabo", password="pass123")

        self.product1 = Product.objects.create(
            name="Coke",
            description="Drink",
            category="Beverage",
            quantity_in_stock=10,
            price=20,
            owner=self.user1
        )

        self.product2 = Product.objects.create(
            name="Bread",
            description="Food",
            category="Bakery",
            quantity_in_stock=15,
            price=15,
            owner=self.user2
        )

    def test_user_sees_only_own_products(self):
        self.client.login(username="jay", password="pass123")

        url = reverse('product-list-create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], "Coke")