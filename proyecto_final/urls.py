from django.contrib import admin
from django.urls import path, include

from proyecto_final.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("", include("proyecto_app.urls"))
]
