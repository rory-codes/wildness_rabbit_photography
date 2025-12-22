from django.contrib import admin
from .models import Collection, Photo, ProductVariant

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_published", "created_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    list_filter = ("is_published",)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "collection", "price", "quality", "is_published", "created_at")
    list_filter = ("collection", "quality", "is_published")
    search_fields = ("title", "description")


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ("photo", "kind", "size", "finish", "price", "currency", "is_active")
    list_filter = ("kind", "size", "finish", "is_active")
    search_fields = ("photo__title", "sku")
