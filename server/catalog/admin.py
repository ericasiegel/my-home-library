from django.contrib import admin
from .generics import annotate_and_prefetch, get_related_names, short_description, create_link_to_changelist
from .models import *


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'book_count', 'books_list']
    search_fields=['name']

    @short_description('Books')
    def books_list(self, author):
        return get_related_names(author, 'author_books')
    
    @short_description('Series')
    def books_list(self, author):
        return get_related_names(author, 'author_series')
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return annotate_and_prefetch(queryset, 'author_books', 'author_books')

    # counting books
    @short_description('Count In Library')
    def book_count(self, author):
        return create_link_to_changelist('admin:catalog_book_changelist', 'authors__id', author, 'book_count')
    

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'book_count']
    search_fields=['type']
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return annotate_and_prefetch(queryset, 'genre_books', 'genre_books')

    @short_description('Count In Library')
    def book_count(self, genre):
       return create_link_to_changelist('admin:catalog_book_changelist', 'genres__id', genre, 'book_count')
    
    
@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'total_books', 'book_count', 'books_list']
    search_fields=['name__icontains', 'author__name__icontains']
    
    @short_description('My Books')
    def books_list(self, series):
        return get_related_names(series, 'series_books')
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return annotate_and_prefetch(queryset, 'series_books', 'series_books')

    # counting books
    @short_description('Count In Library')
    def book_count(self, series):
        return create_link_to_changelist('admin:catalog_book_changelist', 'series__id', series, 'book_count')
    
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'series', 'series_number', 'author_names', 'read', 'description', 'genre_list']
    list_editable = ['read']
    list_per_page = 10
    search_fields = ['title__icontains', 'authors__name__icontains', 'series__name__icontains']
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('authors', 'genres')
    
    @short_description('Author(s)')
    def author_names(self, book):
        return get_related_names(book, 'authors')
    
    @short_description('Genres')
    def genre_list(self, book):
        return get_related_names(book, 'genres')
    