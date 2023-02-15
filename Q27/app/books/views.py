import csv

from django.contrib.postgres.aggregates import StringAgg
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_GET
from django.views.generic import ListView

from .models import Book


class BooksView(ListView):
    template_name = "books.html"
    context_object_name = "books"

    def get_queryset(self):
        title = self.request.GET.get("title", "")
        books = Book.objects.filter(title__icontains=title)
        return books


@require_GET
def export_book_view(request: HttpRequest):
    fields = ["title", "author", "publisher", "published_date", "description"]
    title = request.GET.get("title", "")
    field = request.GET.get("field", "title")
    field = field if field in fields else "title"
    delimiter = request.GET.get("delimiter", ",")
    print(f"hoge{delimiter}hoge", flush=True)
    extension = {",": "csv", " ": "tsv"}

    books = Book.objects.filter(title__icontains=title).aggregate(**{field: StringAgg(field, delimiter=delimiter)})
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="books.{extension.get(delimiter, "csv")}"'

    writer = csv.writer(response, doublequote=False, escapechar=" ", quoting=csv.QUOTE_NONE)
    writer.writerow([books.get(field)])

    return response
