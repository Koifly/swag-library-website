from django.contrib import admin

from .models import BookType, Genre, Book, BookSeries

admin.site.register(BookType)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookSeries)