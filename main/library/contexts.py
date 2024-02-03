from .models import *

# List of all list pages contexts

context_dict = {
    'novels' : {
        'title' : "Novels",
        'intro' : "Some introductory text...",
        'list' : Novel.objects.all()
    },
    'manga' : {
        'title' : "Manga",
        'intro' : "Some introductory text...",
        'list' : Manga.objects.all()
    },
    'comics' : {
        'title' : "Comics",
        'intro' : "Some introductory text...",
        'list' : Comic.objects.all()
    },
    'nonfic' : {
        'title' : "Non-Fiction",
        'intro' : "Some introductory text...",
        'list' : NonFiction.objects.all()
    },
    'all' : {
        'title' : "All books",
        'intro' : "Some introductory text...",
        'list' : Book.objects.all()
    }
}

