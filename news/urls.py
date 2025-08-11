from django.urls import path
from .views import (NewsList, NewsDetail, SearchNews, CreateNews, UpdateNews, DeleteNews, CreateArticles,
                    UpdateArticles, DeleteArticles)

urlpatterns = [
    path('news/', NewsList.as_view(), name='news_list'),
    path('news/<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('news/search/', SearchNews.as_view(), name='news_search'),
    path('news/create/', CreateNews.as_view(), name='news_create'),
    path('news/<int:pk>/update', UpdateNews.as_view(), name='news_update'),
    path('news/<int:pk>/delete', DeleteNews.as_view(), name='news_delete'),

    path('articles/create/', CreateArticles.as_view(), name='articles_create'),
    path('articles/<int:pk>/update', UpdateArticles.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete', DeleteArticles.as_view(), name='articles_delete'),
]
