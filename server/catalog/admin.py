
from django.contrib import admin

from .models import *

# generic function to get a string of any many to many field
def concatenate_related(obj, related_field_name):
    related_objects = getattr(obj, related_field_name).all()
    names = [str(related_obj) for related_obj in related_objects]
    return ', '.join(names)



# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    
@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'series', 'series_number', 'author_names', 'read', 'description', 'genre_list']
    list_editable = ['read']
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('authors', 'genres')
    
    def author_names(self, book):
        return concatenate_related(book, 'authors')
    author_names.short_description = 'Author(s)'
    
    def genre_list(self, book):
        return concatenate_related(book, 'genres')
    genre_list.short_description = 'Genres'
    