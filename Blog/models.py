from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length=100, default='user@email.com')
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name + '-' + self.email


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField()
    categories = models.CharField(max_length=300)
    comment_count = models.IntegerField(null='true')
    like_count = models.IntegerField(null='true')
    icon = models.FileField()
    post_date = models.DateTimeField('posted Date', null='true')

    def __str__(self):
        return self.user + '-' + self.title

    def published_days(self):
        return timezone.now() - self.post_date()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    posts = models.ForeignKey(Posts, on_delete = models.CASCADE)
    comment_text = models.CharField(max_length=500)
    comment_date = models.DateTimeField()

    def __str__(self):
        return self.user + '-' + self.posts
