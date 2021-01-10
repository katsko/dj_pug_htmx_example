from django.shortcuts import render, redirect
from django.http import HttpResponse
from storage import books


def index(request):
    book = books[0]
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


def add_book(request):
    title = request.POST['title']
    book = {'id': len(books) + 1, 'title': title}
    books.append(book)
    if 'HX-Request' not in request.headers:
        return redirect('index')
    return render(request, 'add_book.pug', {'book': book})
