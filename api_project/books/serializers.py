from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):

    search_url = serializers.SerializerMethodField("get_search_url")

    def get_search_url(self, book):
        return f"https://isbnsearch.org/isbn/{book.isbn}"

    class Meta:
        model = Book
        fields = ["id", "title", "author", "isbn", "search_url"]
        depth = 1



class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ["id", "first_name", "last_name", "books"]
        depth = 1
