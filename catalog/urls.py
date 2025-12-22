from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.home, name="home"),
    path("c/<slug:slug>/", views.collection_detail, name="collection"),
    path("p/<int:pk>/", views.photo_detail, name="photo"),
]
