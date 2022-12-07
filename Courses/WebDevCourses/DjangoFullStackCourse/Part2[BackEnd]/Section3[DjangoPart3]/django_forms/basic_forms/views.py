from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from basic_forms import forms

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'basic_forms/index.html')

def form_name_view(request: HttpRequest) -> HttpResponse:
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('VALIDATION SUCCESS')
            print(f"Name: {form.cleaned_data['name']}")
            print(f"Email: {form.cleaned_data['email']}")
            print(f"Text: {form.cleaned_data['text']}")

    return render(request, 'basic_forms/form_page.html', {'form': form})
