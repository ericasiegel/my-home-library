from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('books', views.BookViewSet, basename='books')
router.register('authors', views.AuthorViewSet, basename='authors')
router.register('series', views.SeriesViewSet, basename='series')
router.register('genres', views.GenreViewSet, basename='genres')


urlpatterns = router.urls
