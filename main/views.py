from django.shortcuts import render
from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer

from rest_framework import (
    generics,
    permissions,
    authentication,
    response,
    viewsets
)

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer