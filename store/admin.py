from django.contrib import admin

# Register your models here.
#Pre-built function to add data to models


from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','in_Stock','created','updated']
    list_filter = ['in_Stock','is_Active']
    prepopulated_fields = {'slug': ('name',)}