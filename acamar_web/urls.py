from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

handler404 = "acamar_web.views.handler404"

urlpatterns = [
                  url(r'^api/', include('acamar_web.urls_api', namespace="api")),
                  url(r'^rosetta/', include('rosetta.urls'))
              ] \
              + \
              i18n_patterns(
                  url(r'^404/$', handler404) if settings.DEBUG else None,
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^', include('cms.urls')),
              ) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

