from django.shortcuts import render
from .models import Category, Product


def store(request):
	context = {}
	return render(request, 'store/store.html', context)


def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)


def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)


def categories(request):
    all_categories = Category.objects.all() 
    return {'all_categories': all_categories}


# def product_info(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     context = {'product': product}
#     return render(request, 'store/product-info.html', context)


