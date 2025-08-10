from django.views.generic import ListView, DetailView
from .models import Post
from .filters import SearchFilter


class NewsList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'newslist.html'
    context_object_name = 'newslist'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(post_type='NS')


class NewsDetail(DetailView):
    model = Post
    template_name = 'newsdetail.html'
    context_object_name = 'newsdetail'

    def get_queryset(self):
        return Post.objects.filter(post_type='NS')


class NewsSearch(ListView):
    model = Post
    template_name = 'newssearch.html'
    context_object_name = 'news_search'
    paginate_by = 1


    def get_queryset(self):
        queryset = super().get_queryset().filter(post_type='NS')
        self.filterset = SearchFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
