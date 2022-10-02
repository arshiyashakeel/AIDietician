from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "AI Administration"
admin.site.index_title = "AI Dietician"
admin.site.site_title = "ADMIN PANEL"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("FitMeApp.urls")),
    path("user/", include("user.urls")),
    path("oauth", include("social_django.urls", namespace="social")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
