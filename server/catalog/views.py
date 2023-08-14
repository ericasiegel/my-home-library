from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['authors__id', 'genres__id', 'series__id', 'read']


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class SeriesViewSet(ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author_id']

    
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

