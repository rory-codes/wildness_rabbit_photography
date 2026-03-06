# catalog/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Collection, Photo, ProductVariant
from django.db.models import Min
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from .models import Testimonial
from .forms import TestimonialForm

def testimonials(request):
    qs = Testimonial.objects.filter(is_public=True)

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Please sign in to leave a testimonial.")
            return redirect("account_login")
        form = TestimonialForm(request.POST)
        if form.is_valid():
            t = form.save(commit=False)
            t.user = request.user
            t.save()
            messages.success(request, "Thanks for your testimonial!")
            return redirect("testimonials:index")
    else:
        form = TestimonialForm()

    return render(request, "catalog/testimonials.html", {
        "testimonials": qs,
        "form": form,
    })


def home(request):
    cols = Collection.objects.filter(is_published=True).order_by("name")
    latest_qs = (Photo.objects.filter(is_published=True)
                 .select_related("collection")
                 .order_by("-id")[:12])
    paginator = Paginator(latest_qs, 12)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "catalog/home.html",
        {"collections": cols, 
         },
    )

def collection_detail(request, slug):
    col = get_object_or_404(Collection, slug=slug, is_published=True)
    photos_qs = col.photos.filter(is_published=True).order_by("-created_at")
    paginator = Paginator(photos_qs, 12)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "catalog/collection_detail.html",         
        {
            "collection": col,
            "photos": page_obj.object_list,              
            "page_obj": page_obj,           
        },
    )

def photo_detail(request, pk):
    photo = Photo.objects.get(pk=pk, is_published=True)
    variants = (
        photo.variants
        .filter(is_active=True, stock__gt=0)
        .order_by("kind", "size", "finish")
    )
    digital = variants.filter(kind="digital").first()
    prints = variants.filter(kind="print")
    from_price = variants.aggregate(m=Min("price"))["m"]

    context = {
        "photo": photo,
        "variants": variants,   
        "digital": digital,
        "prints": prints,
        "from_price": from_price,
        "has_variants": variants.exists(),
    }
    return render(request, "catalog/photo_detail.html", context)