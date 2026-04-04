from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart , Order , OrderItem , Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    categories = Product.CATEGORY_CHOICES
    return render(request,'store/home.html',{
        'categories': categories
    })


def products(request):
    category = request.GET.get('category')   # get category from URL

    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    

    return render(request, 'store/product.html', {
        'products': products,
    })

def product_detail (request,pk):
    product = get_object_or_404(Product,pk=pk)
    return render(request,'store/product_detail.html',{"product":product})

@login_required
def add_to_cart (request,pk):
    product = get_object_or_404(Product,pk=pk)

    cart_item,created = Cart.objects.get_or_create(
        user = request.user,
        product = product
    )

    if not created :
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)

    total = 0
    for item in cart_items:
        total += item.total_price

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def remove_cart_item (request,pk):
    cart_item = get_object_or_404(Cart,request.user,pk=pk)
    cart_item.delete()
    return redirect('cart')

@login_required
def update_cart(request,pk,action):
    cart_item = get_object_or_404(Cart,user=request.user,pk=pk)

    if action == 'increase':
        cart_item.quantity += 1
        cart_item.save()
    elif action == 'decrease' :
        cart_item.quantity -= 1 
        if cart_item.quantity > 0 :
            cart_item.save()
        else :
         cart_item.delete()
    return redirect('cart')

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items:
        return redirect('cart')

    total_amount = sum(item.total_price for item in cart_items)

    # Create Order
    order = Order.objects.create(
        user=request.user,
        total_amount=total_amount,
        is_paid=True   # for now we mark as paid
    )

    # Create Order Items
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    # Clear Cart
    cart_items.delete()

    return redirect('order_success')






