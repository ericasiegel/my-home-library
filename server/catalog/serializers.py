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

class GenreTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'type']


# Main Serializers
class GenreSerializer(serializers.ModelSerializer):
    count_in_library = serializers.SerializerMethodField(method_name='calculate_books')
    
    class Meta:
        model = Genre
        fields = ['id', 'type', 'count_in_library']
        
    def calculate_books(self, genre: Genre):
        return genre.genre_books.count()
    
    
class SeriesSerializer(serializers.ModelSerializer):
    count_in_library = serializers.SerializerMethodField(method_name='calculate_books')
    books = BookTitleSerializer(many=True, read_only=True)
    author = AuthorNameSerializer()
    
    class Meta:
        model = Series
        fields = ['id', 'name', 'total_books', 'count_in_library', 'books', 'author']
        
    def calculate_books(self, series: Series):
        return series.series_books.count()
        
          
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
    genres = GenreTypeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'read',  'series', 'series_number', 'authors', 'genres']
    