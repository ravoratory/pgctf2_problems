from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView

from .models import Book


class BooksView(UserPassesTestMixin, ListView):
    template_name = "books.html"
    context_object_name = "books"

    # The world's strongest security
    def test_func(self):
        banned = ["SELECT", "FROM", "WHERE", "LIKE", "%%", "UNION", "JOIN"]
        title = self.request.GET.get("title", "")

        for word in banned:
            if word in title or word.lower() in title:
                return False
        return True

    def get_queryset(self):
        title = self.request.GET.get("title", "")
        books = Book.objects.raw(f"""
            SELECT * FROM books_book
            WHERE title LIKE '%{title}%'
        """)

        return books
