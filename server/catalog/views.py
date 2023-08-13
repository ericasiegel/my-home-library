from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class SeriesViewSet(ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

