from django.urls import path

from .views import BooksView, export_book_view

app_name = "books"
urlpatterns = [
    path("", BooksView.as_view(), name="books"),
    path("export", export_book_view, name="export")
]
