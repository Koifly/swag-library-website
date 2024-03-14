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

def get_series_author(book_list):
    author = book_list[0].author
    for book in book_list:
        if book.author != author:
            author = "Multiple"
            break
    return author

def get_series_owner(book_list):
    owner = book_list[0].get_owner_display()
    for book in book_list:
        if book.get_owner_display() != owner:
            owner = "Multiple"
            break
    return owner


def get_book_list(booktype, genre, user):
    if genre:
        all_books = Book.objects.filter(booktype__booktype=booktype).filter(genre__genre=genre)
    elif booktype:
        all_books = Book.objects.filter(booktype__booktype=booktype)
    elif user:
        all_books = Book.objects.filter(owner=user)
    else:
        all_books = Book.objects.all()

    clean_list = []
    doneSeries = []

    for book in all_books:
        name = book.series.name
        if name == 'None': # Series is None
            clean_list.append(
                {'isSeries':False, 'name':book.title, 'author': book.author, 'owner': book.owner,  'seriesBooks':[book]}
            )
        else:
            if name not in doneSeries:
                doneSeries.append(name)
                books_in_series = all_books.filter(series__name=name)
                author = get_series_author(books_in_series)
                owner = get_series_owner(books_in_series)
                clean_list.append(
                {'isSeries':True, 'name':name, 'author': author, 'owner': owner, 'seriesBooks':books_in_series}
            )

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
        context['list'] = get_book_list(None, None, None)
    else:
        booktype = booktype_url.title()
        if genre_url:
            genre = genre_url.title().replace('_', ' ')
            context['list'] = get_book_list(booktype, genre, None)
        else:
            context['list'] = get_book_list(booktype, None, None)
    return context

def get_user_context(user):
    context = list_context_base['user']
    context['list'] = get_book_list(None, None, user)

    return context
        
