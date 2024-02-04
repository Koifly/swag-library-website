from django import forms
from .models import Book, Genre

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

        if 'booktype' in self.data:
            try:
                booktype_id = int(self.data.get('booktype'))
                self.fields['genre'].queryset = Genre.objects.filter(booktype_id=booktype_id).order_by('genre')
            except (ValueError, TypeError):
                pass 
        elif self.instance.pk:
            self.fields['booktype'].queryset = self.instance.booktype.genre_set.order_by('genre')