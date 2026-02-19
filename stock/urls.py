from django.urls import path
from .views import ProductStockHistoryView, StockMovementCreateView

urlpatterns = [
    path('', StockMovementCreateView.as_view(), name='stock-movement-create'),
    path('history/<int:product_id>/', ProductStockHistoryView.as_view(), name='product-stock-history'),
]
