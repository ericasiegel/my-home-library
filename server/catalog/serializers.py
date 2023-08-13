from rest_framework import serializers
from django.db.models import Count
from .models import *


# Serializers for nested objects
class BookTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']
        
class AuthorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class SeriesNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ['id', 'name']


# General Serializers
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'type']
        
          
class AuthorSerializer(serializers.ModelSerializer):
    count_in_library = serializers.SerializerMethodField(method_name='calculate_books')
    author_books = BookTitleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'count_in_library', 'author_books']
        
    def calculate_books(self, author: Author):
        return author.author_books.count()
    
    
class BookSerializer(serializers.ModelSerializer):
    authors = AuthorNameSerializer(many=True, read_only=True)
    series = SeriesNameSerializer()
    genres = GenreSerializer(many=True, read_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'read',  'series', 'series_number', 'authors', 'genres']
    