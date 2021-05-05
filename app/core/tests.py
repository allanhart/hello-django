from django.test import TestCase
from .models import (
    Album,
    Artist,
    Song,
)


class ArtistTestCase(TestCase):
    def setUp(self):
        self.album = Artist.objects.create(name="Ride the Lightning")

    def test_artist_create(self):
        self.assertEqual(Artist.objects.count(), 1)


