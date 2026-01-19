from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "paid", "stripe_session_id", "created_at")
    list_filter = ("paid",)
    search_fields = ("email", "stripe_session_id")

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "variant", "qty", "price")
    search_fields = ("order__id", "variant__name", "variant__photo__title")