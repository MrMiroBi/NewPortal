from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post



class NewsList(ListView):
    model = Post
    template_name = 'newslist.html'
    context_object_name = 'newslist'


class NewsDetail(DetailView):
    model = Post
    template_name = 'newsdetail.html'
    context_object_name = 'newsdetail'

