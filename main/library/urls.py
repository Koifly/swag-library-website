from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("new-book", views.new_book, name="new-book"),
    path("new-book/<slug:book>", views.new_book),
    path("ajax/load-genres/", views.load_genres, name="ajax_load_genres"),

    path("<slug:booktype>", views.list),
    path("<slug:booktype>/<slug:genre>", views.list),
]