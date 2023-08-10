from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    
class Genre(models.Model):
    type = models.CharField(max_length=255)
    
class Series(models.Model):
    name = models.CharField(max_length=255)
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    series = models.ForeignKey(Series, null=True, on_delete=models.CASCADE, related_name='series_books')
    author = models.ManyToManyField(Author, related_name='author_books')
    read = models.BooleanField(default=False)
    description = models.CharField(max_length=500)
    genre = models.ManyToManyField(Genre, related_name='genre_books')
    # picture = models.ImageField()
    