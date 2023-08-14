from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['authors__id', 'genres__id', 'series__id', 'read']
    search_fields = ['title', 'series__name', 'authors__name', 'genres__type']


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'author_books__title', 'author_series__name']
    
class SeriesViewSet(ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['author_id']
    search_fields = ['name', 'author__name']

    
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

