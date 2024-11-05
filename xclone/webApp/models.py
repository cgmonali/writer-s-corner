from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField( default="slug")

    def __str__(self):
        return self.headline
    

class Writer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.name


class ArticleWriter(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE  , related_name="article_writers")
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name="written_articles")
    role = models.CharField(max_length=100)
    
    def __str__(self):
        return self.role
    

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)