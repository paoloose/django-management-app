from rest_framework import serializers
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer[Article]):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'published')
