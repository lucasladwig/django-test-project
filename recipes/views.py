from django.http import HttpResponse
from django.shortcuts import render


def home(request) -> HttpResponse:
    return render(request, "home.html")


def about(request) -> HttpResponse:
    return HttpResponse("Hi, I'm a ABOUT page.")


def contact(request) -> HttpResponse:
    return HttpResponse("Hi, I'm a CONTACT page.")
