from django.contrib import admin

from articles.models import Article

# This registers the Article resource in the admin panel
admin.site.register(Article)
