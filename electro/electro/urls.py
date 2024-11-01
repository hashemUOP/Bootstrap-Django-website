from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),           # Admin path should come first
    path('', include('home.urls')),            # Home page (root URL)
    path('account/', include('account.urls')), # Account-related URLs
    path('category/', include('cat.urls')),    # Category-related URLs
    path('products/', include('products.urls')), # Product-related URLs
    path('shopping/',include('shopping.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)