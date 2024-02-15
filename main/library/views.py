import os

from .contexts import get_list_context, header_context
from .forms import AddBook, AddGenre, EditBook, BorrowBook
from .models import Book, Genre, BookType

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
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
def book_form(request, book=None):
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
            bookform = AddBook()
    context = header_context | {'bookform': bookform, 'book': book_instance}
    return render(request, 'forms/book_form.html', context)

@login_required(login_url="/login/")
def availability(request):
    book = Book.objects.get(pk=request.POST["book_id"])
    if book.status == "U":
        book.status = "Y"
    else:
        book.status = "U"
        book.borrower = "N"

    book.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url="/login/")
def borrow(request):
    book = Book.objects.get(pk=request.POST["book_id"])
    if book.status == "Y":
        book.status = "O"
        book.borrower = request.user.first_name[0]

    elif book.status == "O" and (request.user.first_name[0] == book.borrower or request.user.first_name[0] == book.owner):
        book.status = "Y";
        book.borrower = "N"

    book.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url="/login/")
def list(request, booktype="all", genre=None):
    template = loader.get_template('list.html')

    list_context = get_list_context(booktype, genre)
    context = header_context | list_context
    
    return HttpResponse(template.render(context, request))