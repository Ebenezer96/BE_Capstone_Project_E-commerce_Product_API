from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# ✅ FIXED IMPORT (THIS IS THE KEY)
from products.views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="product")
router.register("categories", CategoryViewSet, basename="category")
router.register("orders", OrderViewSet, basename="order")


urlpatterns = [
    path("admin/", admin.site.urls),

    # API routes
    path("api/", include(router.urls)),

    # JWT auth
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
