from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.mail import send_mail
import stripe
from orders.models import Order

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig = request.META.get("HTTP_STRIPE_SIGNATURE", "")
    try:
        event = stripe.Webhook.construct_event(payload, sig, settings.STRIPE_WEBHOOK_SECRET)
    except Exception:
        return HttpResponseBadRequest()

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        try:
            order = Order.objects.get(stripe_session_id=session["id"])
            if not order.paid:
                order.paid = True
                order.save()

                # fire-and-forget confirmation 
                if order.email:
                    send_mail(
                        subject="Your Wilderness Rabbit order",
                        message="Thanks for your order! We’ll be in touch soon.",
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[order.email],
                        fail_silently=True,
                    )
        except Order.DoesNotExist:
            pass
    return HttpResponse(status=200)
