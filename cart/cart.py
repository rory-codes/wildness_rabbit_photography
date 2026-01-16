from decimal import Decimal
from django.conf import settings

CART_SESSION_KEY = "cart"

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_KEY)
        if cart is None:
            cart = {}
            self.session[CART_SESSION_KEY] = cart
        self.cart = cart