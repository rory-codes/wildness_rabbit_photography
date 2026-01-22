from django.shortcuts import render
from .models import Testimonial

def index(request):
    items = Testimonial.objects.filter(is_published=True).order_by("-created_at")
    return render(request, "testimonials/index.html", {"items": items})