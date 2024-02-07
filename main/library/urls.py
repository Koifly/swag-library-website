from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("<slug:booktype>", views.list),
    path("<slug:booktype>/<slug:genre>", views.list),
    path("all", views.list, name="all"),

    path("new-book", views.new_book, name="new-book"),
    path("ajax/load-genres/", views.load_genres, name="ajax_load_genres"),
]