from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request,'index.html')
def list_products(request):

    """
    return products list page
    """
    product_list=Product.objects.all()
    product_paginator=Paginator(product_list,2)
    product_list=product_paginator.get_page(1)
    context={'products':product_list}
    return render(request,'products.html',context)
def detail_product(request):
    return render(request,'product_detail.html')