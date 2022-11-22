from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    my_dict = {'insert_val': 'Value from views.py'}
    
    return render(request, 'first_app/index.html', context=my_dict)

def help(request: HttpRequest) -> HttpResponse:
    help_dict = {'help_text': 'Help Page'}

    return render(request, 'first_app/help.html', context=help_dict)
