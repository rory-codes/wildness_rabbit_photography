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

    def add(self, variant_id, price, qty=1):
        key = str(variant_id)
        line = self.cart.get(key, {"qty": 0, "price": str(price)})
        line["qty"] = int(line["qty"]) + int(qty)
        line["price"] = str(price)
        self.cart[key] = line
        self.session.modified = True

    def remove(self, variant_id):
        key = str(variant_id)
        if key in self.cart:
            del self.cart[key]
            self.session.modified = True

    def clear(self):
        self.session[CART_SESSION_KEY] = {}
        self.session.modified = True

    def __iter__(self):
        from catalog.models import ProductVariant
        variant_ids = [int(k) for k in self.cart.keys()]
        variants = {v.id: v for v in ProductVariant.objects.filter(id__in=variant_ids)}
        for key, data in self.cart.items():
            variant = variants.get(int(key))
            if not variant:
                continue
            price = Decimal(data["price"])
            qty = int(data["qty"])
            yield {
                "variant": variant,
                "qty": qty,
                "price": price,
                "subtotal": price * qty,
            }