from .models import Book, BookSeries, BookType

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

context_dict = {
    'novels' : {
        'title' : "Novels",
        'intro' : "Find your fiction novels, novellas and short story collections here.",
        'list' : get_list("Novel")
    },
    'manga' : {
        'title' : "Manga",
        'intro' : "Not to be confused with comics.",
        'list' : get_list("Manga")
    },
    'comics' : {
        'title' : "Comics",
        'intro' : "Superheroes, supervillains and more.",
        'list' : get_list("Comic")
    },
    'nonfic' : {
        'title' : "Non-Fiction",
        'intro' : "Find a topic to learn about.",
        'list' : get_list("Non-Fiction")
    },
    'all' : {
        'title' : "All books",
        'intro' : "That's a lot of books man!",
        'list' : Book.objects.all()
    }
}

