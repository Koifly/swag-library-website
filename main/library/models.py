from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=30)

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
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    owner = models.CharField(max_length=1, choices=OWNER_CHOICES, default="None")
    blurb = models.CharField(max_length=1000, blank=True, default='')
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="Available")


class Novel(Book):
    GENRE_CHOICES = {
        "OTH" : "Other",
        "ADV" : "Adventure",
        "CRI" : "Crime",
        "FAN" : "Fantasy",
        "FOL" : "Folklore",
        "HOR" : "Horror",
        "ROM" : "Romance",
        "SAT" : "Satire",
        "SCI" : "Science-Fiction",
        "THR" : "Thriller",
        "YA" : "Y/A",
    }
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES, default="Other")

class Manga(Book):
    GENRE_CHOICES = {
        "OTH" : "Other",
        "ADV" : "Adventure",
        "CRI" : "Crime",
        "FAN" : "Fantasy",
        "HOR" : "Horror",
        "ROM" : "Romance",
        "SCI" : "Science-Fiction",
        "SHJ" : "Shoujo",
        "SHN" : "Shounen",
        "THR" : "Thriller",
    }
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES, default="Other")

class Comic(Book):
    GENRE_CHOICES = {
        "OTH" : "Other",
        "BAT" : "Batman",
    }
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES, default="Other")

class NonFiction(Book):
    GENRE_CHOICES = {
        "OTH" : "Other",
        "ART" : "Art",
        "ARC" : "Architecture",
        "BOT" : "Botany",
        "CLI" : "Climate",
        "FIN" : "Finance",
        "FIL" : "Film",
        "HIS" : "History",
        "HIT" : "Historical text",
        "MAT" : "Maths",
        "PHI" : "Philosophy",
        "PHY" : "Physics",
        "POL" : "Politics",
        "SOC" : "Sociology",
        "TEC" : "Technology",
    }
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES, default="Other")