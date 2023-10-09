from django.contrib.auth.models import User
from rest_framework import generics, permissions

from articles.models import Article
from articles.serializers import ArticleSerializer

class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer: ArticleSerializer):
        print(self.request.user)
        serializer.save()

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
