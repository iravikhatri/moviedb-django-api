from django.db import models


class Genre(models.Model):

    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Movie(models.Model):

    name = models.CharField(max_length=64)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    director = models.CharField(max_length=64)
    genres = models.ManyToManyField(Genre, related_name='genres', blank=True)

    def __str__(self):
        return self.name