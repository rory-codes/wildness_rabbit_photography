from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

GBP = "GBP"
CURRENCY_CHOICES = [(GBP, "GBP")]

QUALITY_CHOICES = [
    ("standard", "Standard"),
    ("premium", "Premium"),
]

VARIANT_KIND = [
    ("digital", "Digital"),
    ("print", "Print"),
]

PRINT_SIZES = [("A5", "A5"), ("A4", "A4"), ("A3", "A3")]
PRINT_FINISHES = [("matte", "Matte"), ("gloss", "Gloss")]


class Collection(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Photo(models.Model):
    collection = models.ForeignKey(
        Collection, on_delete=models.PROTECT, related_name="photos"
    )
    title = models.CharField(max_length=160)
    description = models.TextField(blank=True)
    image = CloudinaryField("image")
    price = models.DecimalField(max_digits=9, decimal_places=2)  # base price
    quality = models.CharField(max_length=10, choices=QUALITY_CHOICES, default="standard")
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class ProductVariant(models.Model):
    """Each purchasable SKU (digital or a specific print size/finish)."""
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="variants")
    sku = models.CharField(max_length=64, unique=True)
    kind = models.CharField(max_length=10, choices=VARIANT_KIND)
    size = models.CharField(max_length=10, blank=True)    # for prints
    finish = models.CharField(max_length=10, blank=True)  # for prints
    price = models.DecimalField(max_digits=9, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=GBP)
    is_active = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(null=True, blank=True)  # prints only
    # digital file to deliver post-purchase 
    download_asset = models.FileField(upload_to="downloads/", blank=True)
    stripe_price_id = models.CharField(max_length=64, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["photo", "size", "finish", "kind"],
                name="unique_variant_per_photo_size_finish_kind",
            ),
        ]

    def __str__(self):
        return f"{self.photo.title} • {self.kind.upper()} {self.size or ''} {self.finish or ''}".strip()
