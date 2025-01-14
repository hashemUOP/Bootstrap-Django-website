from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
# if admin page doesn't work replace MEDIA_URL and MEDIA_ROOT in settings.py with the comments under
# then after admin working return MEDIA_URL and MEDIA_ROOT retuen them back to their first state so images in project dont corrupt
#MEDIA_URL = '/media/'
#MEDIA_ROOT = BASE_DIR / 'technest' / 'images' / 'products'
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('category/', include('cat.urls')),
    path('products/', include('products.urls')),
    path('shopping/', include('shopping.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

