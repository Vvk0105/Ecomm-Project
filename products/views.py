from django.shortcuts import render
from . models import Product
# Create your views here.
def index(request):
    return render(request,'index.html')
def list_products(request):

    """
    return products list page
    """
    product_list=Product.objects.all()
    context={'products':product_list}
    return render(request,'products.html',context)
def detail_product(request):
    return render(request,'product_detail.html')