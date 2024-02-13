import os

from .contexts import get_list_context, header_context
from .forms import AddBook, AddGenre
from .models import Genre, BookType

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
def new_book(request):
    if request.method == "POST":
        bookform = AddBook(request.POST)
        genreform = AddGenre(request.POST)
        if bookform.is_valid():
            messages.info(request, 'Your book has been added!')
            bookform.save()
            return redirect("/all")

    else:
        bookform = AddBook()
        genreform = AddGenre()
    context = header_context | {'bookform': bookform, 'genreform': genreform}
    return render(request, 'new_book.html', context)


@login_required(login_url="/login/")
def list(request, booktype="all", genre=None):
    template = loader.get_template('list.html')

    list_context = get_list_context(booktype, genre)
    context = header_context | list_context
    
    return HttpResponse(template.render(context, request))