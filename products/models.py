from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify


class Category(models.Model):
    # Human-readable category name (e.g. Electronics, Clothing)
    # Unique to prevent duplicates
    name = models.CharField(max_length=100, unique=True)

    # URL-friendly version of the name
    # Used for clean URLs and searching
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    # Timestamp for auditing and ordering
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Categories should appear alphabetically
        ordering = ["name"]

    def save(self, *args, **kwargs):
        # Automatically generate slug from name if not provided
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        # What shows up in admin and shell
        return self.name


class Product(models.Model):
    # Product title shown to users
    name = models.CharField(max_length=200)

    # Optional long description
    description = models.TextField(blank=True)

    # Monetary value — DecimalField avoids floating-point errors
    # Validator ensures price is never negative
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    # Each product must belong to a category
    # PROTECT prevents deleting a category that still has products
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products"
    )

    # Inventory count
    # PositiveIntegerField guarantees >= 0 at DB level
    stock_quantity = models.PositiveIntegerField()

    # External image URL (can later be replaced with ImageField)
    image_url = models.URLField(blank=True)

    # Creation timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically updates whenever the product is modified
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Newest products appear first
        ordering = ["-created_at"]

        # Database indexes for faster search & filtering
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["price"]),
        ]

    def __str__(self):
        # Useful for admin, logs, and debugging
        return self.name
