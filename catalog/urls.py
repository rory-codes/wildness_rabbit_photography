from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.home, name="home"),
    path("collection/<slug:slug>/", views.collection_detail, name="collection_detail"),
    path("photo/<int:pk>/", views.photo_detail, name="photo_detail"),
]
