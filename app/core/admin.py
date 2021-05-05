from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import (
    Album,
    Artist,
    Song,
)
User = get_user_model()


@admin.register(User)
class ApplicationUserAdmin(UserAdmin):
    list_display = ('email', 'full_name', 'date_joined', 'is_active', 'is_staff',)
    list_filter = ('is_superuser', 'is_staff', 'is_active', 'groups',)
    ordering = ('first_name',)
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone',)

    filter_horizontal = ('groups', 'user_permissions',)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    fields = ('title',)
    list_display = ('title',)
    search_fields = ('title',)

