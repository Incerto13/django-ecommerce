import json
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()

    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('shop:product_list')
    else:
        form = UserCreationForm()
    return render(request, 'shop/signup_form.html', {'form': form})


def verify_form(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.GET.get('value', 0))
    print(product.stock,quantity)
    if product.stock >= quantity:
        response = {'message': 'ok'}
    else:
        response = {
            'message': 'error',
            'error': (
                'You selected an amount greater than the Inventory Stock.<br/>'
                '<strong>Kindly select a value less than {}.</strong>'
            ).format(product.stock)
        }
    return HttpResponse(json.dumps(response), content_type="application/json")