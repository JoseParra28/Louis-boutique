from django.urls import path
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	# Dinamic links for each product
    # path('product/<slug:slug>/', views.product_info, name='product-info'),
]
