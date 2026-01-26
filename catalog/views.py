# catalog/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Collection, Photo, ProductVariant
from django.db.models import Min

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
    variants = photo.variants.all().order_by("kind", "size", "finish")
    digital = variants.filter(kind="digital").first()
    prints = variants.filter(kind="print")

    from_price = variants.aggregate(m=Min("price"))["m"]

    context = {
        "photo": photo,
        "digital": digital,
        "prints": prints,
        "from_price": from_price,
        "has_variants": variants.exists(),
    }
    return render(request, "catalog/photo_detail.html", context)
