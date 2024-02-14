from django.db import models
from taggit.managers import TaggableManager

class BookType(models.Model):
    booktype = models.CharField(max_length=30)

    @property
    def url(self):
        return f'{self.booktype}'.lower()

    def __str__(self):
        return f'{self.booktype}'

class Genre(models.Model):
    booktype = models.ForeignKey(BookType, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)

    @property
    def url(self):
        return f'{self.genre}'.lower()

    class Meta:
        ordering = ['genre']

    def __str__(self):
        return f'{self.genre}:{self.booktype}'

class BookSeries(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    STATUS_CHOICES = {
        "Y" : "Available",
        "O" : "On Loan",
        "R" : "Reserved",
        "U" : "Unavailable",
    }
    OWNER_CHOICES = {
        "R" : "Rayen",
        "D" : "Don",
        "C" : "Charlie",
        "S" : "Sam",
        "H" : "Honey",
        "A" : "Ash",
        "O" : "Soph",
    }
    title = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    booktype = models.ForeignKey(BookType, on_delete=models.CASCADE, related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    owner = models.CharField(max_length=1, choices=OWNER_CHOICES, default="None")
    blurb = models.CharField(max_length=1000, blank=True, default='')
    tags = TaggableManager()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="Available")
    # series = models.ForeignKey(BookSeries, on_delete=models.CASCADE, related_name='books')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title}:{self.author}'