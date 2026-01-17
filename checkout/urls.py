from django.urls import path
from . import views, webhooks 

app_name = "checkout"

urlpatterns = [
    path("start/", views.start_checkout, name="start"),
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel"),
    path("webhook/", webhooks.stripe_webhook, name="webhook"),
]
