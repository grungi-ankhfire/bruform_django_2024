from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.
class AuthorView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
