from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = ("id", "name", "slug", "created_at")

    # Automatically fill slug field from name
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Columns shown in the product list
    list_display = (
        "id",
        "name",
        "category",
        "price",
        "stock_quantity",
        "created_at",
    )

    # Sidebar filters for quick narrowing
    list_filter = ("category", "created_at")

    # Enables search box in admin
    search_fields = ("name",)
