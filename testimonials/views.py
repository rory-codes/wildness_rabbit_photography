from django.shortcuts import get_object_or_404, redirect, render
from .forms import TestimonialForm
from .models import Testimonial

def index(request):
    items = Testimonial.objects.filter(is_published=True).order_by("-created_at")
    form = TestimonialForm()

    return render(
        request,
        "testimonials/index.html",
        {
            "items": items,
            "form": form,
        },
    )


def create_testimonial(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("testimonials:index")
    else:
        form = TestimonialForm()

    items = Testimonial.objects.filter(is_published=True).order_by("-created_at")
    return render(
        request,
        "testimonials/index.html",
        {
            "items": items,
            "form": form,
        },
    )

def edit_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)

    if request.method == "POST":
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect("testimonials:index")
    else:
        form = TestimonialForm(instance=testimonial)

    return render(
        request,
        "testimonials/edit_testimonial.html",
        {
            "form": form,
            "testimonial": testimonial,
        },
    )


def delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)

    if request.method == "POST":
        testimonial.delete()
        return redirect("testimonials:index")

    return render(
        request,
        "testimonials/delete_testimonial.html",
        {
            "testimonial": testimonial,
        },
    )