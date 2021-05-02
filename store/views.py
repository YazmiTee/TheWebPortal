from django.shortcuts import get_object_or_404, render 

from .models import Category, Product

# Create your views here.Allows you to see data in the models on the HTML pages aka templates


def product_all(request):
    products = Product.products.all() # query on the products table and collecting the data from that table. Same as mySQL SELECT ALL from PRODUCTS
    return render(request, 'store/home.html', {'products': products}) # render means load template. Take request, take the template and merge with data then return to website
    
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_Stock=True) # if the item isn't instock it will show 404 error. SQL query select the product where the slug == slug and in_stock == True
    return render(request, 'store/products/single.html', { 'product': product})

def category_list(request, category_slug):
    category =get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter (category=category)
    return render (request, 'store/products/category.html', {'category':category, 'products':products})