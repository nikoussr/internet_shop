from django.shortcuts import render, redirect
from shop.models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart  # импорт корзины

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(customer=request.user.username)
            total = 0
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price_at_order=item['price']
                )
                total += item['price'] * item['quantity']
            order.total_amount = total
            order.save()
            cart.clear()
            return redirect('orders:order_success', order_id=order.id)  # ✅ имя маршрута из urls.py

    else:
        form = OrderCreateForm()
    return render(request, 'create.html', {'cart': cart, 'form': form})

def order_success(request, order_id):
    return render(request, 'created.html', {'order_id': order_id})
