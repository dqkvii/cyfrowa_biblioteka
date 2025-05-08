from django.db import models

from django.db import models


class Book(models.Model):
    GENRE_CHOICES = [
        ('fantasy', 'Fantasy'),
        ('sci-fi', 'Science Fiction'),
        ('drama', 'Drama'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ('horror', 'Horror'),
        ('other', 'Other'),
    ]

    YEAR_CHOICES = [(year, year) for year in range(1800, 2025)]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.IntegerField(choices=YEAR_CHOICES, default=2023)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='other')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title