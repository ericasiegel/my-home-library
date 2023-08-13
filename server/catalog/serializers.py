from rest_framework import serializers
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
    author = AuthorNameSerializer(read_only=True)
    
    get_authors = serializers.PrimaryKeyRelatedField(source='author', queryset=Author.objects.all(), write_only=True)
    
    class Meta:
        model = Series
        fields = ['id', 'name', 'total_books', 'count_in_library', 'books', 'author', 'get_authors']
        
    def calculate_books(self, series: Series):
        return series.series_books.count()
    
    def create(self, validated_data):
        author = validated_data.pop('author', None) # Note the change to 'author'

        series = Series.objects.create(**validated_data, author=author) # Assign the author directly
        series.save()
        return series

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('get_authors', None)
        return representation

        
          
class AuthorSerializer(serializers.ModelSerializer):
    count_in_library = serializers.SerializerMethodField(method_name='calculate_books')
    books = BookTitleSerializer(source='author_books', many=True, read_only=True) # Fixed here
    series = SeriesNameSerializer(source='author_series', many=True, read_only=True) # And here
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'count_in_library', 'books', 'series']
        
    def calculate_books(self, author: Author):
        return author.author_books.count()

    
    
class BookSerializer(serializers.ModelSerializer):
    get_authors = serializers.PrimaryKeyRelatedField(source='authors', many=True, queryset=Author.objects.all(), write_only=True)
    get_series = serializers.PrimaryKeyRelatedField(source='series', allow_null=True, required=False, queryset=Series.objects.all(), write_only=True)
    get_genres = serializers.PrimaryKeyRelatedField(source='genres', many=True, queryset=Genre.objects.all(), write_only=True)

    authors = AuthorNameSerializer(many=True, read_only=True)
    series = SeriesNameSerializer(read_only=True)
    genres = GenreTypeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'read', 'series', 'series_number', 'get_authors', 'get_genres', 'get_series', 'authors', 'genres']

    def create(self, validated_data):
        authors = validated_data.pop('authors')
        genres = validated_data.pop('genres')
        series = validated_data.pop('series', None)

        book = Book.objects.create(**validated_data)
        book.authors.set(authors)
        book.genres.set(genres)
        book.series = series
        book.save()
        return book

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('get_authors', None)
        representation.pop('get_series', None)
        representation.pop('get_genres', None)
        return representation



    