from store.models import Product



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
        
        self.session.modified = True # updates session with modified data

    def __len__(self):
        """
        Get basket and count the quatity in the basket
        """
        return sum(item['qty'] for item in self.basket.values())  # counts all the values of the key qty
