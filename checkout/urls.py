from django.urls import path
from . import views

app_name = "checkout"

urlpatterns = [
    path("start/", views.start_checkout, name="start"),
    path("success/", views.success, name="success"),
]
