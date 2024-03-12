from .models import *
from django.db.models import Q

header_context = {
    'booktypelist' : BookType.objects.filter(~Q(booktype="Series")),
    'genrelist' : Genre.objects.all(),
}

# List of all list pages contexts
def series_not_listed(book_list, series):
    for book in book_list:
        if book.title == series.title:
            return False
    return True

def get_book_list(booktype, genre):
    if genre:
        all_books = Book.objects.filter(booktype__booktype=booktype).filter(genre__genre=genre)
    elif booktype:
        all_books = Book.objects.filter(booktype__booktype=booktype)
    else:
        all_books = Book.objects.all()

    clean_list = []
    doneSeries = []

    for book in all_books:
        name = book.series.name
        if name == 'None': # Series is None
            clean_list.append({'isSeries':False, 'name':book.title, 'seriesBooks':[book]})
        else:
            if name not in doneSeries:
                doneSeries.append(name)
                books_in_series = all_books.filter(series__name=name)
                clean_list.append({'isSeries':True, 'name':name, 'seriesBooks':books_in_series})

    clean_list = sorted(clean_list, key=lambda d: d['name'])

    return clean_list


list_context_base = {
    'novel' : {
        'title' : "Novels",
        'intro' : "Find your fiction novels, novellas and short story collections here.",
    },
    'manga' : {
        'title' : "Manga",
        'intro' : "Not to be confused with comics.",
    },
    'comic' : {
        'title' : "Comics",
        'intro' : "Superheroes, supervillains and more.",
    },
    'non-fiction' : {
        'title' : "Non-Fiction",
        'intro' : "Find a topic to learn about.",
    },
    'all' : {
        'title' : "All books",
        'intro' : "That's a lot of books man!",
    },
    'user' : {
        'title' : "My books",
        'intro' : "All the books you've added so far...",
    }
}

def get_list_context(booktype_url, genre_url):
    context = list_context_base[booktype_url]

    if booktype_url == "all":
        context['list'] = get_book_list(None, None)
    else:
        booktype = booktype_url.title()
        if genre_url:
            genre = genre_url.title().replace('_', ' ')
            context['list'] = get_book_list(booktype, genre)
        else:
            context['list'] = get_book_list(booktype, None)
    return context

def get_user_context(user):
    context = list_context_base['user']
    context['list'] = Book.objects.filter(owner=user)

    return context
        
