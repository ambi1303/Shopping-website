from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Home page
    path('product/', include('products.urls')),  # Product page
    path('accounts/', include('accounts.urls')),  # Custom accounts URL
    path('accounts/', include('allauth.urls')),  # Allauth URLs for authentication (login, signup, etc.)
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files in development
urlpatterns += staticfiles_urlpatterns()
