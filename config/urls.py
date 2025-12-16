from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def root(request):
    return JsonResponse({
        "message": "E-commerce Product API",
        "endpoints": {
        "products": "/api/products/",
        "admin": "/admin/"
        }
    })

urlpatterns = [
    path("", root),
    path("admin/", admin.site.urls),
    path("api/", include("products.urls")),
]
