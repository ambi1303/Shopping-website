from django.db.models import Q
from django.shortcuts import render
from products.models import Product, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def index(request):
    products = Product.objects.filter(newest_product=True)
    context = {
        'products': products
    }
    return render(request, 'home/index.html', context)


def search(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(
            Q(product_name__icontains=query) |
            Q(product_desription__icontains=query) |
            Q(category__category_name__icontains=query)
        ).distinct()
    else:
        products = []
    
    context = {
        'products': products,
        'query': query
    }
    return render(request, 'home/search.html', context)


def contact(request):
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')


def terms_and_conditions(request):
    return render(request, 'home/terms.html')


def privacy_policy(request):
    return render(request, 'home/privacy.html')
