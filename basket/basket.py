from store.models import Product
from decimal import Decimal

from django.conf import settings


class Basket():
    """ 
    Provides some default behaviours that can be inherited or overidded
    """

    def __init__(self, request):
        self.session = request.session #
        basket = self.session.get(settings.BASKET_SESSION_ID) # session is retrieved 
        if settings.BASKET_SESSION_ID not in request.session : 
            basket = self.session[settings.BASKET_SESSION_ID] = {} # if there is no session then a new one is created
        self.basket = basket # basket daat stored here  
    

    def add(self, product, qty):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': qty}

        self.save()

    def __iter__(self):
        """
        Collects the product id in session data to query the database & returns the products
        """
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    
    
    def __len__(self):
        """
        Get basket and count the quatity in the basket
        """
        return sum(item['qty'] for item in self.basket.values())  # counts all the values of the key qty
    
    def update(self, product, qty):
        """
        Update values in session data
        """
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        self.save()

    def get_total_price(self):
        """
        calculates the total using the item price * qty for each item in the basket
        """
        subtotal = sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

        if subtotal == 0:
            shipping = Decimal(0.00)
        else:
            shipping = Decimal(11.50)

        total = subtotal + Decimal(shipping)
        return total

    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
            #print(product_id)
            self.save()

    def save(self):
        """
        Saves data to session data table
        """
        self.session.modified = True

    def clear(self):
        # remvoes basket from session
        del self.session[settings.BASKET_SESSION_ID]
        self.save()