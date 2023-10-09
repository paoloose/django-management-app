"""
Authentication and authorization are handled by the default permissions classes:
`rest_framework_simplejwt.authentication.JWTAuthentication`
"""
from rest_framework import generics, permissions

from articles.models import Article
from articles.serializers import ArticleSerializer

class ArticleListCreate(generics.ListCreateAPIView):
    """
    A read/create endpoint for listing and creating articles.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    The read/update/delete endpoint for individual articles.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
