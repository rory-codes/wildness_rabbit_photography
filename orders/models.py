from django.db import models
from django.conf import settings
from catalog.models import ProductVariant  

class Order(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    stripe_session_id = models.CharField(max_length=255, blank=True, null=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)  # captured at time of purchase