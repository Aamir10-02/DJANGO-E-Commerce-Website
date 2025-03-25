from .cart import Cart

#create context processor for our cart to work on every pages

def cart(request):
    # return the default data from the cart
    return {'cart': Cart(request)}  