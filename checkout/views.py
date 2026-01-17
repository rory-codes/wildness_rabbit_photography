from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
import stripe
from cart.cart import Cart  

stripe.api_key = settings.STRIPE_SECRET_KEY

def start_checkout(request):
    cart = Cart(request)
    if cart.count() == 0:
        return redirect("cart:detail")

    line_items = []
    for item in cart:
        variant = item["variant"]      
        qty = int(item["qty"])
        price_pence = int(variant.price * 100)

        line_items.append({
            "price_data": {
                "currency": "gbp",
                "product_data": {"name": f"{variant.photo.title} — {variant.name}"},
                "unit_amount": price_pence,
            },
            "quantity": qty,
        })

    success_url = request.build_absolute_uri(
        reverse("checkout:success")
    ) + "?session_id={CHECKOUT_SESSION_ID}"
    cancel_url = request.build_absolute_uri(reverse("cart:detail"))

    session = stripe.checkout.Session.create(
        mode="payment",
        line_items=line_items,
        success_url=success_url,
        cancel_url=cancel_url,
    )
    return redirect(session.url, permanent=False)

def success(request):
    return render(request, "checkout/success.html")
