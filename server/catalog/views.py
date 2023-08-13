from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
@api_view()
def book_list(request):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def book_detail(request, id):
    book = Book.objects.get(pk=id)
    serializer = BookSerializer(book)
    return Response(serializer.data)



@api_view()
def author_list(request):
    queryset = Author.objects.all()
    serializer = AuthorSerializer(queryset, many=True)
    return Response(serializer.data)
    
@api_view()
def author_detail(request, id):
    author = Author.objects.get(pk=id)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)
