from django import forms
from .models import Book

class AddBook(forms.ModelForm):
  template_name = "new_book_form.html"
  class Meta:
    model = Book
    fields = ["title", "author", "booktype", "genre", "owner", "blurb", "tags"]
    labels = {
        'title': "Title",
        "author": "Author",
        "booktype" : "Type",
        "genre" : "Genre",
        "owner": "Owner",
        "blurb": "Blurb",
        "tags": "Tags",
    }

  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genre'].queryset = Book.objects.none()