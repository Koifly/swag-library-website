from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("novels", views.list, name="novels"),
    path("manga", views.list, name="manga"),
    path("comics", views.list, name="comics"),
    path("nonfic", views.list, name="nonfic"),
    path("all", views.list, name="all"),

    path("new-book", views.new_book, name="new-book"),
    path("ajax/load-genres/", views.load_genres, name="ajax_load_genres"),
]