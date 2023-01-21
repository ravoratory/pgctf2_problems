from django.urls import path

from .views import BooksView

app_name = "books"
urlpatterns = [
    path("", BooksView.as_view(), name="books"),
]
