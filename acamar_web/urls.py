from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from .views import Error404View

handler404 = Error404View.as_view()

urlpatterns = (
    [
        path("api/", include("acamar_web.urls_api", namespace="api")),
        path("rosetta/", include("rosetta.urls")),
    ]
    + i18n_patterns(path("admin/", admin.site.urls), path("", include("cms.urls")))
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
