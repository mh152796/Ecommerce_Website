from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, Order
from shop.models import Products

# Create your views here.

def add_to_cart(request, pk):
    item = get_object_or_404(Products, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1

            order_item[0].save()
            return redirect('index')
        else:
            order.orderitems.add(order_item[0])
            return redirect('index')
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        return redirect('index')

def cart_view(request):
    cart = Cart.objects.filter(user=request.user, purchased=False)
    order = Order.objects.filter(user=request.user, ordered=False)
    if order.exists():
        total = order[0].get_totals()
    else:
        total = 0
    if cart.exists():
        return render(request, 'cart_view.html', {'cart':cart, 'total':total})
    else:
        return ValueError("You haven't an active card")    