# cart/cart.py
from decimal import Decimal
from django.conf import settings
from catalog.models import ProductVariant

CART_SESSION_KEY = "cart"

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_KEY)
        if cart is None:
            cart = {}
            self.session[CART_SESSION_KEY] = cart
        self._cart = cart

    def add(self, variant_id: int, qty: int = 1, override: bool = False):
        key = str(variant_id)
        if key not in self._cart:
            self._cart[key] = {"qty": 0}
        self._cart[key]["qty"] = qty if override else self._cart[key]["qty"] + qty
        if self._cart[key]["qty"] <= 0:
            self._cart.pop(key, None)
        self._save()

    def remove(self, variant_id: int):
        self._cart.pop(str(variant_id), None)
        self._save()

    def clear(self):
        self.session[CART_SESSION_KEY] = {}
        self._cart = {}
        self.session.modified = True

    def _save(self):
        self.session[CART_SESSION_KEY] = self._cart
        self.session.modified = True

    def count(self) -> int:
        return sum(item["qty"] for item in self._cart.values())

    def items(self):
        """Yields dicts: variant, qty, unit_price, subtotal"""
        variant_map = {
            v.id: v for v in ProductVariant.objects.filter(id__in=[int(k) for k in self._cart.keys()])
        }
        for key, data in self._cart.items():
            variant = variant_map.get(int(key))
            if not variant:
                continue
            unit = Decimal(variant.price)
            qty = int(data["qty"])
            yield {
                "variant": variant,
                "qty": qty,
                "unit_price": unit,
                "subtotal": unit * qty,
            }

    def total(self) -> Decimal:
        return sum(item["subtotal"] for item in self.items())
