from store.models import Product, Profile

class Cart():
    def __init__(self, request):
        self.session = request.session
        # Get Request
        self.request = request

        # get the current session key it it exists
        cart = self.session.get('session_key')

        # if the session key does not exist, create a new one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Cart available on all pages

        self.cart = cart

    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = quantity
        if product_id in self.cart:
            pass

        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # Deal With Login User
        if self.request.user.is_authenticated:
            # Get user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert 
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # Save Cart to Profile model
            current_user.update(old_cart=str(carty))

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = quantity
        if product_id in self.cart:
            pass

        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # Deal With Login User
        if self.request.user.is_authenticated:
            # Get user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert 
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # Save Cart to Profile model
            current_user.update(old_cart=str(carty))



    def cart_total(self):
        # Get products id
        product_ids = self.cart.keys()
        # look up products in database
        products = Product.objects.filter(id__in=product_ids)
        # Get quantities
        quantities = self.cart
        # from 0
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total


    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        # Get products from cart
        product_ids = self.cart.keys()

        # use ids to lookup products in database model

        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)   
        outcart = self.cart
        outcart[product_id] = product_qty      
        
        self.session.modified = True
        

        if self.request.user.is_authenticated:
            # Get user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert 
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # Save Cart to Profile model
            current_user.update(old_cart=str(carty))
        thing = self.cart
        return thing
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

        # Deal With Login User
        if self.request.user.is_authenticated:
            # Get user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert 
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # Save Cart to Profile model
            current_user.update(old_cart=str(carty))


# from django.contrib.sessions.models import Session
# session_k = Session.objects.get(pk='lru6bgv4q22rg1jjj51gtr8oe5gn7kkq')
# session_k.get_decoded()