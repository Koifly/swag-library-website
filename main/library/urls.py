from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("novels", views.list, name="novels"),
    path("manga", views.list, name="manga"),
    path("comics", views.list, name="comics"),
    path("nonfic", views.list, name="nonfic"),
    path("all", views.list, name="all"),
]