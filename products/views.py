from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.

class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['category']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'quantity_in_stock', 'created_at']

    def get_queryset(self):
        queryset = Product.objects.filter(owner=self.request.user)

        low_stock = self.request.query_params.get('low_stock')

        if low_stock == 'true':
            queryset = queryset.filter(quantity_in_stock__lte=5)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)