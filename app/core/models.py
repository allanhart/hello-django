from django.contrib.auth.models import AbstractUser
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=30)


class Album(models.Model):
    name = models.CharField(max_length=30)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Song(models.Model):
    title = models.CharField(max_length=30)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


class User(AbstractUser):
    REQUIRED_FIELDS = ('first_name', )

    first_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        if not self.last_name:
            return self.first_name
        return '{} {}'.format(self.first_name, self.last_name)