from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    type = models.CharField(max_length=255)
    
    def __str__(self):
        return self.type
    
class Series(models.Model):
    name = models.CharField(max_length=255, unique=True)
    total_books = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_series')
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    series = models.ForeignKey(Series, blank=True, null=True, on_delete=models.CASCADE, related_name='series_books', )
    series_number = models.IntegerField(blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name='author_books')
    read = models.BooleanField(default=False)
    description = models.CharField(max_length=500)
    genres = models.ManyToManyField(Genre, related_name='genre_books')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # picture = models.ImageField()
    
    def __str__(self):
        return self.title