from store.models import Product
from decimal import Decimal



class Basket():
    """ 
    Provides some default behaviours that can be inherited or overidded
    """

    def __init__(self, request):
        self.session = request.session #
        basket = self.session.get('skey') # session is retrieved 
        if 'skey' not in request.session : 
            basket = self.session['skey'] = {} # if there is no session then a new one is created
        self.basket = basket # baaket daat stored here  
    

    def add(self, product, qty):
        """
        adding & updating session data 
        """
        product_id = product.id

        if product_id not in self.basket :
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty)}
        
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
    
    def get_total_price(self):
        """
        calculates the total using the item price * qty for each item in the basket
        """
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

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
        self.session.modified = True