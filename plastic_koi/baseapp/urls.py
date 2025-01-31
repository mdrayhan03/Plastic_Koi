from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "baseapp"

urlpatterns = [
    path("", views.landpage, name="landpage"),
    path("map/", views.map, name="map"),
    path("upload/", views.upload, name="upload"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)