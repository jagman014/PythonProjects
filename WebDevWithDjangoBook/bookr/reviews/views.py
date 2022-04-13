from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render

from .models import Book, Review
from .utils import average_rating


def book_list(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    book_list = []

    for book in books:
        reviews = book.review_set.all()

        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        
        else:
            book_rating = None
            number_of_reviews = 0
        
        book_list.append(
            {
                'book': book,
                'book_rating': book_rating,
                'number_of_reviews': number_of_reviews
            }
        )
    
    context = {'book_list': book_list}

    return render(request, 'reviews/book_list.html', context)


def book_detail(request: HttpRequest, pk: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()

    if reviews:
        book_rating = average_rating([review.rating for review in reviews])

        context = {
            'book': book,
            'book_rating': book_rating,
            'reviews': reviews
        }
    
    else:
        context = {
            'book': book,
            'book_rating': None,
            'reviews': None
        }
    
    return render(request, 'reviews/book_detail.html', context)
