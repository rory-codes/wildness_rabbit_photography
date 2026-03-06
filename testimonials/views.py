from django.contrib.auth.decorators import login_required
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


@login_required
def create_testimonial(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.name = request.user.username
            testimonial.save()
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


@login_required
def edit_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk, user=request.user)

    if request.method == "POST":
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            updated_testimonial = form.save(commit=False)
            updated_testimonial.user = request.user
            updated_testimonial.name = request.user.username
            updated_testimonial.save()
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


@login_required
def delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk, user=request.user)

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