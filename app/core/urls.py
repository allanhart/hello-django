from django.contrib import admin
from django.urls import path

from .views import (
    ArtistListView,
    ArtistDetailView,
)
urlpatterns = [
    path('artists/', ArtistListView.as_view(), name='artist.list'),
    path('artist/<int:pk>/', ArtistDetailView.as_view(), name='artist.read'),
]
