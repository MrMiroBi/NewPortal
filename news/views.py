from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from .filters import SearchFilter
from .forms import NewsForm, ArticlesForm


class NewsList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(post_type='NS')


class ArticlesList(ListView):
    monel = Post
    ordering = '-date'
    template_name = 'articles/articles_list.html'
    context_object_name = 'articles_list'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(post_type='AR')


class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'news_detail'

    def get_queryset(self):
        return Post.objects.filter(post_type='NS')


class SearchNews(ListView):
    model = Post
    template_name = 'news/search_news.html'
    context_object_name = 'news_search'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset().filter(post_type='NS')
        self.filterset = SearchFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class CreateArticles(CreateView):
    form_class = ArticlesForm
    model = Post
    template_name = 'articles/articles_form.html'


class UpdateArticles(CreateView):
    form_class = ArticlesForm
    model = Post
    template_name = 'articles/articles_form.html'


class DeleteArticles(DeleteView):
    model = Post
    template_name = 'articles/delete_articles.html'
    success_url = reverse_lazy('articles/articls_list')


class CreateNews(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news/news_form.html'


class UpdateNews(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news/news_form.html'


class DeleteNews(DeleteView):
    model = Post
    template_name = 'news/delete_news.html'
    success_url = reverse_lazy('news/news_list')
