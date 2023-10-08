from django.urls import path
from articles import views

urlpatterns = [
    path('', views.articles_list),
    path('<int:pk>/', views.article_detail)
]
