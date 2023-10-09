"""
URL configuration for probaar project.
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

swagger_view = TemplateView.as_view(
    template_name='swagger-ui.html',
    extra_context={'schema_url': 'openapi-schema'}
)

openapi_view = get_schema_view(
    title='Probaar\'s API',
    description='API Swagger endpoint for easily testing!',
    version='0.0.1',
    permission_classes=[],
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('openapi/', openapi_view, name='openapi-schema'),
    path('', swagger_view, name='swagger-ui'),
]
