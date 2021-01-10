from django.contrib import admin
from django.urls import path
from dj_pug_htmx.views import index, get_book_list, get_book, add_book

urlpatterns = [
    path('', index, name='index'),
    path('book/list/', get_book_list, name='get_book_list'),
    path('book/add/', add_book, name='add_book'),
    path('book/<int:book_id>/', get_book, name='get_book'),
]
