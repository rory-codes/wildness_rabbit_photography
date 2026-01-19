from django.conf import settings
from django.http import JsonResponse, Http404
from django.shortcuts import redirect, render
import stripe
from orders.models import Order, OrderItem
from cart.cart import Cart 

stripe.api_key = settings.STRIPE_SECRET_KEY

def start_checkout(request):
    cart = Cart(request)
    if cart.count() == 0:
        return redirect("cart:detail")

    # Create a draft order 
    order = Order.objects.create(email=request.user.email if request.user.is_authenticated else "")

    line_items = []
    for item in cart:
        variant = item["variant"]      
        qty = item["qty"]
        price = int(variant.price * 100)  # pence

        # Save items to order
        OrderItem.objects.create(order=order, variant=variant, qty=qty, price=variant.price)

        line_items.append({
            "price_data": {
                "currency": "gbp",
                "product_data": {"name": f"{variant.photo.title} — {variant.name}"},
                "unit_amount": price,
            },
            "quantity": qty,
        })

    session = stripe.checkout.Session.create(
        mode="payment",
        line_items=line_items,
        success_url=request.build_absolute_uri("/checkout/success?session_id={CHECKOUT_SESSION_ID}"),
        cancel_url=request.build_absolute_uri("/cart/"),
    )
    order.stripe_session_id = session.id
    order.save()
    return redirect(session.url, permanent=False)

def cancel(request):
    return render(request, "checkout/cancel.html")

def success(request):
    """
    Verify the Stripe session is paid; if so, show an order summary and clear cart.
    """
    session_id = request.GET.get("session_id")
    if not session_id:
        return redirect("cart:detail")

    try:
        session = stripe.checkout.Session.retrieve(session_id)
    except Exception:
        return redirect("cart:detail")

    if session.get("payment_status") != "paid":
        return redirect("cart:detail")

    order = None
    items = []
    total = 0

    try:
        order = Order.objects.get(stripe_session_id=session_id)
        order_items = (
            OrderItem.objects
            .filter(order=order)
            .select_related("variant__photo")  
        )
        for it in order_items:
            line_total = it.qty * it.price
            items.append({
                "title": getattr(it.variant.photo, "title", ""),
                "variant": getattr(it.variant, "name", ""),
                "qty": it.qty,
                "price": it.price,
                "line_total": line_total,
            })
            total += line_total

        if not order.paid:
            order.paid = True
            order.save()
    except Order.DoesNotExist:
        pass

    # Clear the cart after a successful payment
    Cart(request).clear()

    return render(
        request,
        "checkout/success.html",
        {"session": session, "order": order, "items": items, "total": total},
    )