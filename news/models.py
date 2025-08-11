from django.db import models
from django.contrib.auth.models import User
from .helper import types, news
from django.utils import timezone
from django.urls import reverse


class Author(models.Model):
    rating = models.IntegerField(default=0)

    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        post = 0
        comment = 0
        post_comment = 0
        for p in self.post_set.all():
            post += p.rating * 3
            if not comment:
                for com in Comment.objects.filter(user=self.author).exclude(post=p):
                    comment += com.rating
                for com in Comment.objects.filter(post=p).exclude(user=self.author):
                    post_comment += com.rating
        self.rating = post + comment + post_comment
        self.save()


class Category(models.Model):
    title = models.CharField(max_length=20, unique=True)


class Post(models.Model):
    post_type = models.CharField(max_length=2, choices=types, default=news)
    date = models.DateTimeField(default=timezone.now)
    head = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    post_like = models.IntegerField(default=0)
    post_dislike = models.IntegerField(default=0)

    post_category = models.ManyToManyField(Category, through="PostCat")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def like(self):
        self.rating += 1
        self.post_like += 1
        self.save()

    def dislike(self):
        if self.rating != 0:
            self.rating -= 1
            self.post_dislike += 1
            self.save()

    def preview(self):
        return f'{self.text[:124]}...' if len(self.text) > 124 else self.text

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


    def __str__(self):
        return f'Author - {self.author.author}: {self.head}'


class PostCat(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(default=0)
    comment_like = models.IntegerField(default=0)
    comment_dislike = models.IntegerField(default=0)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.comment_like += 1
        self.save()

    def dislike(self):
        if self.rating != 0:
            self.rating -= 1
            self.comment_dislike += 1
            self.save()
