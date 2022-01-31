from django.urls import path, include
from . import views

urlpatterns = [
   path('add_to_cart/<str:pk>/', views.add_to_cart, name='add_to_cart'),
   path('cart_view/', views.cart_view, name='cart_view'),
]