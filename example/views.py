from django.utils.translation import gettext as _
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, "example/dashboard.html", context={'page_title': 'Dashboard v1'})


def contacts(request: HttpRequest) -> HttpResponse:
    return render(request, "example/contacts.html")


def register(request: HttpRequest) -> HttpResponse:
    return render(request, "example/register.html")


def term_of_use(request: HttpRequest) -> HttpResponse:
    return render(request, "example/term_of_use.html")
