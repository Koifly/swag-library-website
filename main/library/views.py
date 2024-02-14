import os

from .contexts import get_list_context, header_context
from .forms import AddBook, AddGenre, EditBook
from .models import Book, Genre, BookType

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def home(request):
    context = header_context
    return render(request, "home.html", context)

@login_required(login_url="/login/")
def load_genres(request):
    booktype = request.GET.get('booktype')
    genres = Genre.objects.filter(booktype=booktype).order_by('genre')
    return render(request, 'hr/genre_list_options.html', {'genres': genres})

@login_required(login_url="/login/")
def new_book(request, book=None):
    book_instance = None
    if request.method == "POST":
        if book:
            book_instance = Book.objects.get(id=book)
            bookform = EditBook(
                request.POST,
                instance=book_instance
            )
        else:
            bookform = bookform = AddBook(request.POST)
        if bookform.is_valid():
            bookform.save()
            return redirect("/all")
    else:
        if book:
            book_instance = Book.objects.get(id=book)
            bookform = EditBook(instance=book_instance)
        else:
            bookform = bookform = AddBook()
    context = header_context | {'bookform': bookform, 'book': book_instance}
    return render(request, 'new_book.html', context)


@login_required(login_url="/login/")
def list(request, booktype="all", genre=None):
    template = loader.get_template('list.html')

    list_context = get_list_context(booktype, genre)
    context = header_context | list_context
    
    return HttpResponse(template.render(context, request))