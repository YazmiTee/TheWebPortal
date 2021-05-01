from django.urls import path

from . import views #. means from the same folder. views 

app_name = 'store' # connectiing it to the namespace stroe in the core urls

urlpatterns = [
    path('',views.all_products,name ='all_products'),
    
]
