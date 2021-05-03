from .basket import Basket # basket class imported


def basket(request): # request is used because it holds info in the http request - session included
    return {'basket': Basket(request)} # returns the basket data from the class