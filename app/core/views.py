from django.views.generic import (
    DetailView,
    ListView,
)
from .models import Artist


class ArtistListView(ListView):
    model = Artist
    context_object_name = 'artist_list'


class ArtistDetailView(DetailView):
    model = Artist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foo'] = 'bar'
        return context


