from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_queryset(self):
        queryset = Book.objects.all()
        authors_id = self.request.query_params.get('authors_id')
        genres_id = self.request.query_params.get('genres_id')
        series_id = self.request.query_params.get('series_id')
        
        if authors_id is not None: 
            queryset = queryset.filter(authors__id=authors_id)
        if genres_id is not None: 
            queryset = queryset.filter(genres__id=genres_id)
        if series_id is not None: 
            queryset = queryset.filter(series__id=series_id)
        
        return queryset

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class SeriesViewSet(ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

    def get_queryset(self):
        queryset = Series.objects.all()
        author_id = self.request.query_params.get('author_id')
        if author_id is not None: 
            queryset = queryset.filter(author_id=author_id)
        
        return queryset
    
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

