from django.urls import path
from . import views


urlpatterns = [
    path('authors/', views.author_list),
    path('authors/<int:id>/', views.author_detail),
    path('books/', views.book_list),
    path('books/<int:id>/', views.book_detail),
    path('genres/', views.genre_list),
    path('genres/<int:id>/', views.genre_detail),
    path('series/', views.series_list),
    path('series/<int:id>/', views.series_detail),
]
