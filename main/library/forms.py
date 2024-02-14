from django import forms
from taggit.forms import *
from .models import Book, Genre


class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author","owner", "booktype", "genre", "blurb", "tags"]
        labels = {
            "title": "Title",
            "author": "Author",
            "owner": "Owner",
            "booktype": "Book type",
            "genre": "Genre",
            "blurb": "Blurb",
            "tags": "Tags",
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'text-input',
                'placeholder': 'Title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'text-input',
                'placeholder': 'Author'
            }),
            'owner': forms.Select(attrs={
                'class': 'text-input'
            }),
            'booktype': forms.Select(attrs={
                'class': 'text-input'
            }),
            'genre': forms.Select(attrs={
                'class': 'text-input'
            }),
            'blurb': forms.Textarea(attrs={
                'class': 'text-input',
                'placeholder': 'Optional, maximum 1000 characters.'
            }),
            'tags': forms.TextInput(attrs={
                'class': 'text-input',
                'placeholder': 'Write your tags here, separated by commmas.'
            })
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

class EditBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author","owner", "booktype", "genre", "blurb", "tags"]
        labels = {
            "title": "Title",
            "author": "Author",
            "owner": "Owner",
            "booktype": "Book type",
            "genre": "Genre",
            "blurb": "Blurb",
            "tags": "Tags",
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'text-input',
                'placeholder': 'Title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'text-input',
                'placeholder': 'Author'
            }),
            'owner': forms.Select(attrs={
                'class': 'text-input'
            }),
            'booktype': forms.Select(attrs={
                'class': 'text-input'
            }),
            'genre': forms.Select(attrs={
                'class': 'text-input'
            }),
            'blurb': forms.Textarea(attrs={
                'class': 'text-input',
                'placeholder': 'Optional, maximum 1000 characters.'
            }),
            'tags': forms.TextInput(attrs={
                'class': 'text-input',
                'placeholder': 'Write your tags here, separated by commmas.'
            })
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['booktype'].disabled = True
            self.fields['genre'].disabled = True

class EditBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["status"]

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class AddGenre(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ["genre"]
        labels = {
            "genre": "Genre",
        }