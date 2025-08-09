from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'newslist.html'
    context_object_name = 'newslist'
    paginate_by = 10
    def get_queryset(self):
        return Post.objects.filter(post_type = 'NS')


class NewsDetail(DetailView):
    model = Post
    template_name = 'newsdetail.html'
    context_object_name = 'newsdetail'


    def get_queryset(self):
        return Post.objects.filter(post_type = 'NS')

