from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
urlpatterns = [

    # Django admin
    path("admin/", admin.site.urls),

    # API apps
    path("api/accounts/", include("accounts.urls")),
    path("api/", include("posts.urls")),

    # JWT
    path("api/login/", 
         include("rest_framework.urls")),

    # Swagger
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema"
    ),
    path(
    "api/login/",
    TokenObtainPairView.as_view(),
    name="token_obtain_pair"
),

path(
    "api/token/refresh/",
    TokenRefreshView.as_view(),
    name="token_refresh"
),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui"
    ),

    
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )