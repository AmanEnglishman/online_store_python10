from django.urls import path
from .views import add_to_cart, cart_view, decrease_quantity, increase_quantity, remove_from_cart

urlpatterns = [
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('', cart_view, name='cart'),
    path('decrease-quantity/<int:item_id>', decrease_quantity, name='decrease_quantity'),
    path('increase-quantity/<int:item_id>', increase_quantity, name='increase_quantity'),
    path('remove/<int:item_id>', remove_from_cart, name='remove_from_cart'),
]