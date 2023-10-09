"""
URL configuration for probaar project.
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.authentication import JWTAuthentication

swagger_view = TemplateView.as_view(
    template_name='swagger-ui.html',
    extra_context={'schema_url': 'openapi-schema'}
)

# # define jwt authentication
# openapi_view = get_schema_view(
#     title='Probaar\'s API',
#     description='API Swagger endpoint for easily testing!',
#     version='0.0.1',
#     permission_classes=[],
#     public=True,
#     authentication_classes=(JWTAuthentication,),
#     renderer_classes=['openapi', 'swagger']
# )

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin-dashboard'),
    path('api/', include('api.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(), name='openapi-schema'),
]
