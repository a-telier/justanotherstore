from django.shortcuts import render, redirect, reverse  #  renders HTML templates
from django.http import HttpResponse #  displays HttpResponse
from django.shortcuts import render
from django.contrib import messages
from products.models import Product


# Create your views here.
def view_cart(request):
    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} ({product.quantity}) to your shopping cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):

    try:
        cart = request.session.get('cart', {})
        
        cart.pop(item_id)
        request.session['cart'] = cart
        return HttpResponse(status=200)
        
    except Exception as e:
        return HttpResponse(status=500)