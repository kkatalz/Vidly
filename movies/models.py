from django.db import models
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=255)  # type: ignore

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)  # type: ignore
    release_year = models.IntegerField()  # type: ignore
    number_in_stock = models.IntegerField()  # type: ignore
    daily_rate = models.FloatField()  # type: ignore
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)  # type: ignore
    date_created = models.DateTimeField(default=timezone.now)  # type: ignore
