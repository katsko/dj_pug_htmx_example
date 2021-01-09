from django.shortcuts import render
from django.http import HttpResponse
from storage import books


def index(request):
    book = {'id': 1, 'title': books[0]['title']}
    return render(
        request, 'base.pug',
        {
            'book': book,
            'book_list': books,
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
    template = 'book.pug'
    book = {'id': book_id, 'title': books[book_id - 1]['title']}
    context = {'book': book, 'set_title': True}
    if 'HX-Request' not in request.headers:
        template = 'base.pug'
        context['book_list'] = books
        context['set_title'] = False
    return render(request, template, context)
