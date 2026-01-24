from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from .cart import Cart
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
    # POSTed from the photo page
    variant_id = request.POST.get("variant_id")
    if not variant_id:
        return redirect("cart:detail")

    try:
        quantity = int(request.POST.get("quantity", "1"))
        if quantity < 1:
            quantity = 1
    except (TypeError, ValueError):
        quantity = 1

    variant = get_object_or_404(ProductVariant, pk=variant_id)

    cart = Cart(request)
    cart.add(variant_id=variant.id, qty=quantity, override=False)

    return redirect("cart:detail")

@require_POST
def update(request, variant_id: int):
    try:
        qty = int(request.POST.get("quantity", "1"))
        if qty < 1:
            qty = 1
    except (TypeError, ValueError):
        qty = 1

    # make sure the variant exists
    variant = get_object_or_404(ProductVariant, pk=variant_id)

    cart = Cart(request)
    # Same param names as in add()
    cart.add(variant_id=variant.id, qty=qty, override=True)

    return redirect(reverse("cart:detail"))

@require_POST
def remove(request, variant_id: int):
    cart = Cart(request)
    cart.remove(variant_id)
    return redirect(reverse("cart:detail"))

@require_POST
def clear(request):
    Cart(request).clear()
    return redirect(reverse("cart:detail"))