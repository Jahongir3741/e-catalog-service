from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Arxiv Elektron catalog API",
        default_version='v1',
        description="Test description",
        contact=openapi.Contact(email="contact@snippets.local"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authentication.urls')),
    path("api/v1/", include("main.urls")),
    path("api/v1/", include('helper.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
