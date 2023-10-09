from django.urls import path
from articles import views

urlpatterns = [
    path('', views.ArticleListCreate.as_view(), name='article-list'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='article-detail'),
]
