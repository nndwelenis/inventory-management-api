from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Supplier

# 🧠 What This Tests

# Authenticated user can create supplier
# 201 is returned
# Supplier actually saved in database


# Create your tests here.
class SupplierAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="jay", password="pass123")
        self.client.login(username="jay", password="pass123")

    def test_create_supplier(self):
        url = reverse('supplier-list-create')

        data = {
            "name": "ABC Distributors",
            "contact_email": "abc@test.com",
            "phone_number": "0123456789"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), 1)
        self.assertEqual(Supplier.objects.first().name, "ABC Distributors")