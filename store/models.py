from django.db import models
from django.urls import reverse
# to import User model use - from django.contrib.auth,models import User

# Create your models here. 
# #Classes- the template to creat the tables in the database
#Category table- clas describes the attributes

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_Active=True)

class Category(models.Model): # extends from model to give use the functionality that models has
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255,unique= True) # slug allows you to write the name of the cat in the url

    class Meta: # metadata about 
        verbose_name_plural = 'categories' # Django will add an S at the end of the class name so setting it do it is gramatically correct
    
    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])
    
    def __str__(self):
        return self.name #returns the data as string in the table



#Prodcuts table
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete= models.CASCADE) # foreign key from category table, on_delete says if therre isnt a category then it will delete the product
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to ='images/' , default='images/default.jpg') #Images not stored in Db, online the link to images (stroed in project folder)
    slug = models.SlugField(max_length=255) # can be used to write the product name in the URL and then be taken straight to that products page
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_Stock = models.BooleanField(default=True)
    is_Active = models.BooleanField(default=True) # if people can by it?
    created = models.DateField(auto_now_add=True) # records the date it was added to store
    updated = models.DateTimeField(auto_now=True) # triggered eevytime I make a new update *refreshes the date & time
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',) # sorted in decending order based on when it wasa created
    
    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])
    
    
    def __str__(self):
        return self.name