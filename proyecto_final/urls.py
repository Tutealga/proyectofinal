from django.contrib import admin
from django.urls import path, include

from proyecto_final.views import index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("", include("proyecto_app.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
