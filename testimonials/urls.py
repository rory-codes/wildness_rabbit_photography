from django.urls import path
from . import views

app_name = "testimonials"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.create_testimonial, name="add"),
    path("edit/<int:pk>/", views.edit_testimonial, name="edit"),
    path("delete/<int:pk>/", views.delete_testimonial, name="delete"),
    ]