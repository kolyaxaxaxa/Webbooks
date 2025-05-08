from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse('<h1>Главная страница сайта «Мир книг»!</h1>')


def book_by_id(request, book_id):
    return HttpResponse(f'<h2>Книга # {book_id}</h2>')


def book_by_slug(request, book_slug):
    return HttpResponse(f'<h2>Ссылка www.site.ru/book/{book_slug}</h2>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')