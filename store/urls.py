from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products",views.products, name="products"),
    path("product_details/<int:pk>/", views.product_detail, name="product_detail"),
    path("add-to-cart/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart_view, name="cart"),
    path("remove-cart-item/<int:pk>/", views.remove_cart_item, name="remove_cart_item"),
    path('update-cart/<int:pk>/<str:action>/', views.update_cart, name='update_cart'),
    path("checkout/", views.checkout, name="checkout"),
]

