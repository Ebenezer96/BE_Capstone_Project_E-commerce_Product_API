from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for product categories.
    Exposes minimal, safe data.
    """

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "created_at",
        ]
        read_only_fields = ["id", "slug", "created_at"]


class ProductSerializer(serializers.ModelSerializer):
    """
    Main serializer for products.
    Handles validation and API representation.
    """

    # Readable category info for frontend display
    category_detail = CategorySerializer(
        source="category",
        read_only=True
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "category",          # write-only reference
            "category_detail",   # read-only nested data
            "stock_quantity",
            "image_url",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    # --------------------
    # Field-level validation
    # --------------------

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Product name cannot be empty."
            )
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Price must be greater than or equal to 0."
            )
        return value

    def validate_stock_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Stock quantity cannot be negative."
            )
        return value
