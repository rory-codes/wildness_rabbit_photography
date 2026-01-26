from django.urls import path
from . import views
from catalog.views import testimonials

app_name = "catalog"

urlpatterns = [
    path("", views.home, name="index"),  
    path("", views.home, name="home"), 
    path("collections/<slug:slug>/", views.collection_detail, name="collection"),
    path("photos/<int:pk>/", views.photo_detail, name="photo"),
    path("testimonials/", views.testimonials, name="testimonials"),
]
