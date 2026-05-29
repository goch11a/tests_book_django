from rest_framework import generics
from .models import Book, Author
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend


class AuthorViewset(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_fields = ['natinolity']
    filter_backends = [DjangoFilterBackend]
   

class BookViewset(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]    