from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("book", views.book_form),
    path("book/edit-id:<slug:book>", views.book_form),
    path("borrow", views.borrow, name="borrow"),
    path("availability", views.availability, name="availability"),
    path("ajax/load-genres/", views.load_genres, name="ajax_load_genres"),

    path("<slug:booktype>", views.list),
    path("<slug:booktype>/<slug:genre>", views.list),
]