from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .filters import ProductFilter
from .models import Order


# -----------------------------
# Custom Permission
# -----------------------------
class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


# -----------------------------
# Category ViewSet
# -----------------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -----------------------------
# Product ViewSet
# -----------------------------
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = ProductFilter
    search_fields = ["name"]
    ordering_fields = ["price", "created_at"]

    # -----------------------------
    # Purchase Endpoint (STEP 9 FIXED)
    # -----------------------------
@action(
    detail=True,
    methods=["post"],
    permission_classes=[permissions.IsAuthenticated],
)
def purchase(self, request, pk=None):
    quantity = int(request.data.get("quantity", 1))

    if quantity < 1:
        return Response(
            {"detail": "Invalid quantity"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    with transaction.atomic():
        product = Product.objects.select_for_update().get(pk=pk)

        if product.stock_quantity < quantity:
            return Response(
                {"detail": "Insufficient stock"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        product.stock_quantity -= quantity
        product.save()

        order = Order.objects.create(
            user=request.user,
            product=product,
            quantity=quantity,
            total_price=product.price * quantity,
        )

    return Response(
        {
            "detail": "Order placed successfully",
            "order_id": order.id,
            "remaining_stock": product.stock_quantity,
        },
        status=status.HTTP_201_CREATED,
    )