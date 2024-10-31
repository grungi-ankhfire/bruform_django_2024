from django.urls import path
from . import views

urlpatterns = [
    path("authors/", views.AuthorView.as_view(), name="author-list"),
    path("books/", views.BookView.as_view(), name="book-list"),
]
