

from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category

def store(request, category_slug =None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_avilable=True)
    else:
        products = Product.objects.filter(is_avilable=True)
        
    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)

# def product_detail(request, category_slug, product_slug):
#     try:
#         single_product = Product.objects.get(category_slug =category_slug, slug=product_slug)
#     except Exception as e:
#         raise e

#     context={
#         'single_product' : single_product,
#         }

#     return render(request, 'store/product_detail.html',context)


def product_detail(request, category_slug, product_slug):
    try:
        # Get the Category instance using the category_slug
        category = get_object_or_404(Category, slug=category_slug)
        
        # Get the Product instance using both category and product slugs
        single_product = get_object_or_404(Product, category=category, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }

    return render(request, 'store/product_detail.html', context)


