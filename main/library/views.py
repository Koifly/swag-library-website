import os

from .contexts import context_dict
from .forms import AddBook
from .models import Genre

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def home(request):
    return render(request, "home.html")

@login_required(login_url="/login/")
def load_genres(request):
    booktype = request.GET.get('booktype')
    genres = Genre.objects.filter(booktype=booktype).order_by('genre')
    return render(request, 'hr/genre_list_options.html', {'genres': genres})

@login_required(login_url="/login/")
def new_book(request):
    if request.method == "POST":
        form = AddBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddBook()
    return render(request, 'new_book_form.html', {'form': form})

def get_list_type(request):
    path = request.path
    list_type = os.path.basename(os.path.normpath(path))
    return list_type

def build_context(request):
    list_type = get_list_type(request)

    context = context_dict[list_type]

    return context

@login_required(login_url="/login/")
def list(request):
    template = loader.get_template('list.html')
    context = build_context(request)
    
    return HttpResponse(template.render(context, request))