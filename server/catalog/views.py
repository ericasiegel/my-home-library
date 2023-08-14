from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['authors__id', 'genres__id', 'series__id', 'read']
    search_fields = ['title', 'series__name', 'authors__name', 'genres__type']
    ordering_fields = ['title', 'authors__name', 'series__name']


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'author_books__title', 'author_series__name']
    ordering_fields = ['name', 'author_books__title', 'author_series__name']
    
class SeriesViewSet(ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['author_id']
    search_fields = ['name', 'author__name']
    ordering_fields = ['name', 'author__name']

    
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['type']
