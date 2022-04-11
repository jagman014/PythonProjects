from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'base.html')


def search(request: HttpRequest) -> HttpResponse:
    search_input = request.GET.get('search')
    return render(request, 'search.html', {'search_input': search_input})
