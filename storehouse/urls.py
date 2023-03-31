from django.urls import include, path

from rest_framework.routers import DefaultRouter

from storehouse import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"order", views.OrderViewSet, basename="order")
router.register(r"product", views.ProductViewSet, basename="product")
router.register(r"users", views.UserViewSet, basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
