from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view()
def author_list(request):
    return Response('ok')
    
@api_view()
def author_detail(request, id):
    return Response(id)
