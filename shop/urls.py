from django.urls import path
from .views import *

urlpatterns = [
    path('', AllProducts.as_view(), name='all_products'),
    path('products/<slug:slug>', ProductDetail.as_view(), name='product_detail'),
    # path('<slug:slug>', product_detail, name='product_detail'),
    path('cart/detail', cart_detail, name='cart-detail'),
    path('cart/add/<product_id>', cart_add, name='cart-add'),
    path('cart/remove/<product_id>', cart_remove, name='cart-remove'),
    path('create_order', CreateOrder1.as_view(), name='create_order'),
    path('confirmation/orders/<int:id>', ConfirmationView.as_view(), name='confirmation'),
]