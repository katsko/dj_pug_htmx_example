from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse('abc')
    return render(
        request, 'base.pug',
        {
            'book_id': 1,
        }
    )


def get_book_list(request):
    return render(
        request, 'book_list.pug',
        {
            'base_template': 'base.pug',
        }
    )


def get_book(request, book_id):
    template = 'base.pug'
    if 'HX-Request' in request.headers:
        template = 'book.pug'
    return render(request, template, {'book_id': book_id})
