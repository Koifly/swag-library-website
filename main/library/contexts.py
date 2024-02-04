from .models import Book

# List of all list pages contexts

context_dict = {
    'novels' : {
        'title' : "Novels",
        'intro' : "Find your fiction novels, novellas and short story collections here.",
        'list' : Book.objects.filter(booktype__booktype="Novel")
    },
    'manga' : {
        'title' : "Manga",
        'intro' : "Not to be confused with comics.",
        'list' : Book.objects.filter(booktype__booktype="Manga")
    },
    'comics' : {
        'title' : "Comics",
        'intro' : "Superheroes, supervillains and more.",
        'list' : Book.objects.filter(booktype__booktype="Comic")
    },
    'nonfic' : {
        'title' : "Non-Fiction",
        'intro' : "Find a topic to learn about.",
        'list' : Book.objects.filter(booktype__booktype="Non-Fiction")
    },
    'all' : {
        'title' : "All books",
        'intro' : "That's a lot of books man!",
        'list' : Book.objects.all()
    }
}

