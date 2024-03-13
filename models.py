from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 30)
    rating = models.IntegerField(default = 0)
    User = models.ForeignKey(Author, on_delete = models.CASCADE)

class Category(models.Model):
    name = models.CharField(unique = True,max_lenght = 20)

class Post(models.Model):
    Author = models.ForeignKey(Author, on_delete = models.CASCADE)
    datetime = models.DateTimeField(auto_now_add)
    title = models.CharField(default = 0)
    text = models.TextField(unique = True,default = 0)
    rating = models.IntegerField(default=0)

    Category = models.ManyToManyField(Product, through='PostCategory')

class PostCategory(models.Model):
    Post = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    Category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField(unique=True, default=0)
    some_datetime = models.DateTimeField(auto_now_add)
    rating = models.IntegerField(default=0)
    Post = models.ForeignKey(Comment, on_delete=models.CASCADE)
    User = models.ForeignKey(Comment, on_delete=models.CASCADE)