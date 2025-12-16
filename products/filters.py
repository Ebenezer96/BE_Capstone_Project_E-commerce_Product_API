import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    """
    Custom filters for product listing.
    """

    min_price = django_filters.NumberFilter(
        field_name="price",
        lookup_expr="gte"
    )
    max_price = django_filters.NumberFilter(
        field_name="price",
        lookup_expr="lte"
    )

    in_stock = django_filters.BooleanFilter(
        method="filter_in_stock"
    )

    def filter_in_stock(self, queryset, name, value):
        if value is True:
            return queryset.filter(stock_quantity__gt=0)
        if value is False:
            return queryset.filter(stock_quantity__lte=0)
        return queryset

    class Meta:
        model = Product
        fields = ["category"]
