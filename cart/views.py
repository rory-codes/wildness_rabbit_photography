from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from .cart import Cart
from .forms import AddToCartForm
from catalog.models import ProductVariant

def detail(request):
    cart = Cart(request)
    context = {
        "items": list(cart.items()),
        "total": cart.total(),
    }
    return render(request, "cart/detail.html", context)

@require_POST
def add(request):
    form = AddToCartForm(request.POST)
    if form.is_valid():
        variant = get_object_or_404(ProductVariant, pk=form.cleaned_data["variant_id"], is_active=True)
        qty = form.cleaned_data["quantity"]
        Cart(request).add(variant.id, qty=qty)
    return redirect(reverse("cart:detail"))

@require_POST
def update(request, variant_id: int):
    qty = int(request.POST.get("quantity", "1"))
    Cart(request).add(variant_id, qty=qty, override=True)
    return redirect(reverse("cart:detail"))

@require_POST
def remove(request, variant_id: int):
    Cart(request).remove(variant_id)
    return redirect(reverse("cart:detail"))

@require_POST
def clear(request):
    Cart(request).clear()
    return redirect(reverse("cart:detail"))
