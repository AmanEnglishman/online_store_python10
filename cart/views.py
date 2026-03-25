from django.shortcuts import render, redirect, get_object_or_404

from .models import CartItem, Cart
from products.models import Product

def add_to_cart(request, product_id):

    if not request.user.is_authenticated:
        return redirect('login')

    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item , created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('product_detail', pk=product_id)

def cart_view(request):

    cart = Cart.objects.filter(user=request.user).first()
    items = cart.items.all() if cart else []
    total = sum(item.get_total_price() for item in items)

    context = {'cart': cart, 'items': items, 'total': total}

    return render(request, 'cart/cart.html', context)