from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
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
            order.paid = True
            order.save()
        except Order.DoesNotExist:
            pass
    return HttpResponse(status=200)
