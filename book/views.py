from rest_framework import generics
from .models import Book, Author
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import permissions


class AuthorViewset(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
   

class BookViewset(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]    