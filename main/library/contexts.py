from .models import Book, BookSeries, BookType, Genre
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

def get_list(book_type):
    all_books = list(Book.objects.filter(booktype__booktype=book_type))
    book_list = all_books
    # TODO: support book series
    
    # for book in all_books:
    #     if book.series.name != "None":
    #         series = Book(
    #             title=book.series.name,
    #             author=book.author,
    #             booktype=BookType(booktype="Series"),
    #             genre=book.genre, owner=book.owner,
    #             series=book.series
    #         )
    #         book_list.remove(book)
    #         if series_not_listed(book_list, series):
    #             book_list.append(series)
    return book_list

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
        context['list'] = Book.objects.all()
    else:
        booktype = booktype_url.title()
        if genre_url:
            genre = genre_url.title().replace('_', ' ')
            context['list'] = Book.objects.filter(booktype__booktype=booktype).filter(genre__genre=genre)
        else:
            context['list'] = Book.objects.filter(booktype__booktype=booktype)

    return context

def get_user_context(user):
    context = list_context_base['user']
    context['list'] = Book.objects.filter(owner=user)

    return context
        
