from django import forms
from taggit.forms import *
from .models import Book, Genre, BookSeries


class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author","owner", "booktype", "genre", "series", "volume", "blurb", "tags"]
        labels = {
            "title": "Title",
            "author": "Author",
            "owner": "Owner",
            "booktype": "Book type",
            "genre": "Genre",
            "series": "Series",
            "volume": "Volume",
            "blurb": "Blurb",
            "tags": "Tags",
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Author'
            }),
            'owner': forms.Select(attrs={
                'class': 'form-input'
            }),
            'booktype': forms.Select(attrs={
                'class': 'form-input'
            }),
            'genre': forms.Select(attrs={
                'class': 'form-input'
            }),
            'series': forms.Select(attrs={
                'class': 'form-input'
            }),
            'volume': forms.TextInput(attrs={
                'type':'number',
                'class': 'form-input'
            }),
            'blurb': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Optional, maximum 1000 characters.'
            }),
            'tags': forms.TextInput(attrs={
                'class': 'form-input',
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
        fields = ["title", "author","owner", "booktype", "genre", "series", "volume", "blurb", "tags"]
        labels = {
            "title": "Title",
            "author": "Author",
            "owner": "Owner",
            "booktype": "Book type",
            "genre": "Genre",
            "series": "Series",
            "volume": "Volume",
            "blurb": "Blurb",
            "tags": "Tags",
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Author'
            }),
            'owner': forms.Select(attrs={
                'class': 'form-input'
            }),
            'booktype': forms.Select(attrs={
                'class': 'form-input'
            }),
            'genre': forms.Select(attrs={
                'class': 'form-input'
            }),
            'blurb': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Optional, maximum 1000 characters.'
            }),
            'tags': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Write your tags here, separated by commmas.'
            })
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['booktype'].disabled = True
            self.fields['genre'].disabled = True

class BorrowBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["status", "borrower"]
        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-input'
            }),
            'borrower': forms.Select(attrs={
                'class': 'form-input'
            })
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class AddGenre(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ["booktype", "genre"]
        labels = {
            "booktype": "Booktype",
            "genre": "Genre",
        }

        widgets = {
            'booktype': forms.Select(attrs={
                'class': 'form-input'
            }),
            'genre': forms.TextInput(attrs={
                'class': 'form-input'
            })
        }

class AddSeries(forms.ModelForm):
    class Meta:
        model = BookSeries
        fields = ["name"]
        labels = {
            "name": "Series name"
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input'
            })
        }