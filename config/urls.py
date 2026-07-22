"""
URL configuration for config project.

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
from webluvra import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', views.all_products_random, name='all_products_random'),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path('', include('webluvra.urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


