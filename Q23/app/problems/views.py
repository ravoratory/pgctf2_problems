import os

from django.http import HttpRequest, HttpResponse
from django.template import engines

FLAG = os.getenv("FLAG")


def index(request: HttpRequest) -> HttpResponse:
    engine = engines["django"]
    param = request.GET.get("param", "")  # !!!
    template = engine.from_string(f"<html><h1>Hello, World!</h1>{param}</html>")

    return HttpResponse(template.render({"flag": FLAG}, request))
