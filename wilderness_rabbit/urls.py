"""
URL configuration for wilderness_rabbit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from catalog import views as catalog_views

urlpatterns = [
    #path("", catalog_views.home, name="home"),
    path("", include(("catalog.urls", "catalog"), namespace="catalog")),
    path("accounts/profile/", RedirectView.as_view(url="/", permanent=False)),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path("cart/", include(("cart.urls", "cart"), namespace="cart")),
    path("checkout/", include(("checkout.urls", "checkout"), namespace="checkout")),
    path("enquiries/", include(("enquiries.urls", "enquiries"), namespace="enquiries")),
    path("orders/", include("orders.urls")),
    path("testimonials/", include(("testimonials.urls", "testimonials"), namespace="testimonials")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
