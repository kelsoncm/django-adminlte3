from django.utils.translation import gettext as _
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, "adminlte3/dashboard.html", context={'page_title': 'Dashboard v1'})


def contacts(request: HttpRequest) -> HttpResponse:
    return render(request, "adminlte3/contacts.html")


def register(request: HttpRequest) -> HttpResponse:
    return render(request, "adminlte3/register.html")


def term_of_use(request: HttpRequest) -> HttpResponse:
    return render(request, "adminlte3/term_of_use.html")
