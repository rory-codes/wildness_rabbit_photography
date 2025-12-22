from django.shortcuts import render, get_object_or_404
from .models import Collection, Photo, ProductVariant

def home(request):
    cols = Collection.objects.filter(is_published=True).order_by("name")
    latest = Photo.objects.filter(is_published=True).select_related("collection")[:12]
    return render(request, "catalog/home.html", {"collections": cols, "latest": latest})

def collection_detail(request, slug):
    col = get_object_or_404(Collection, slug=slug, is_published=True)
    photos = col.photos.filter(is_published=True)
    return render(request, "catalog/collection_detail.html", {"collection": col, "photos": photos})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk, is_published=True)
    variants = photo.variants.filter(is_active=True)
    return render(request, "catalog/photo_detail.html", {"photo": photo, "variants": variants})
