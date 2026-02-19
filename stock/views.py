from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.db import transaction

from .models import StockMovement
from .serializers import StockMovementSerializer
from products.models import Product

# Create your views here.

class StockMovementCreateView(generics.CreateAPIView):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        movement_type = serializer.validated_data['movement_type']
        quantity = serializer.validated_data['quantity']

        # Ensure product belongs to the logged-in user
        if product.owner != self.request.user:
            raise ValidationError("You cannot modify stock for a product you do not own.")

        if movement_type == 'IN':
            product.quantity_in_stock += quantity

        elif movement_type == 'OUT':
            if quantity > product.quantity_in_stock:
                raise ValidationError("Insufficient stock.")
            product.quantity_in_stock -= quantity

        product.save()

        serializer.save(performed_by=self.request.user)