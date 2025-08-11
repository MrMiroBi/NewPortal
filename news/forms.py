from django import forms
from .models import Post


class NewsForm(forms.ModelForm):
    post_type = forms.CharField(widget=forms.HiddenInput(), initial='NS')

    class Meta:
        model = Post
        fields = [
            'head',
            'text',
            'post_type',
        ]


class ArticlesForm(forms.ModelForm):
    post_type = forms.CharField(widget=forms.HiddenInput(), initial='AR')

    class Meta:
        model = Post
        fields = [
            'head',
            'text',
            'post_type',
        ]
