from django.urls import path
from .views import AuthorViewset, BookViewset



urlpatterns = [
    path('authors/', AuthorViewset.as_view(), name="author-list"),
    path('books/', BookViewset.as_view(), name='book-list')    
]


