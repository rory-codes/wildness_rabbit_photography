from django.db import models
from django.conf import settings
from catalog.models import ProductVariant  

class Order(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    stripe_session_id = models.CharField(max_length=255, blank=True, null=True)