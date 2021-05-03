from django.urls import path

from . import views #. means from the same folder. views 

app_name = 'store' # connectiing it to the namespace stroe in the core urls

urlpatterns = [
    path('',views.product_all,name ='product_all'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'), #<slug:slug> refer to <variable (datatype): Data (From table)>
    path('search/<slug:category_slug>/', views.category_list, name="category_list")
    
]
