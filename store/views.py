from django.shortcuts import render
from .models import Category, Product

# Create your views here.Allows you to see data in the models on the HTML pages aka templates
def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all() # query on the products table and collecting the data from that table. Same as mySQL SELECT ALL from PRODUCTS
    return render(request, 'store/home.html', {'products': products}) # render means load template. Take request, take the template and merge with data then return to website