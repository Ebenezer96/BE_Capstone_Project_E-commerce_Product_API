from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .filters import ProductFilter


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing product categories.
    - Read: public
    - Write: authenticated users only
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing products.
    - Read: public
    - Write: authenticated users only
    """

    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filtering, searching, ordering
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = ProductFilter
    search_fields = [
        "name",
        "category__name",
        "category__slug",
    ]
    ordering_fields = [
        "price",
        "created_at",
        "stock_quantity",
    ]
    ordering = ["-created_at"]
