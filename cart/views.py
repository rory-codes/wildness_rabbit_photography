from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import ProductVariant
from .cart import Cart

def detail(request):
    cart = Cart(request)
    return render(request, "cart/detail.html", {"cart": cart})

@require_POST
def add(request, variant_id):
    variant = get_object_or_404(ProductVariant, pk=variant_id, is_active=True)
    qty = int(request.POST.get("qty", 1))
    Cart(request).add(variant.id, variant.price, qty)
    return redirect("cart:detail")

@require_POST
def remove(request, variant_id):
    Cart(request).remove(variant_id)
    return redirect("cart:detail")