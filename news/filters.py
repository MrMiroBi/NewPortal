from django_filters import FilterSet, CharFilter, DateFilter
from django.forms import DateInput
from .models import Post


class SearchFilter(FilterSet):
    author = CharFilter(
        field_name='author__author__username',
        lookup_expr='icontains',
        label='Автор'
    )

    head = CharFilter(
        field_name='head',
        lookup_expr='icontains',
        label='Заголовок'
    )
    date = DateFilter(
        field_name='date',
        lookup_expr='gt',
        label='Позже указанной даты',
        widget=DateInput(attrs={'type': 'date'}),
    )

    class Meta:
        madel = Post
        fields = ['author', 'head', 'pub_date']
