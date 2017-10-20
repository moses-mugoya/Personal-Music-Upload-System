from django.contrib import admin

from music.models import Song, DailyQuotes, BibleQuotes, Comment, Lyric


class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'songFile', 'artist', 'publish')

admin.site.register(Song, SongAdmin)


class DailyAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'publish', 'artist')

admin.site.register(DailyQuotes, DailyAdmin)


class BibleAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'publish', 'artist')

admin.site.register(BibleQuotes, BibleAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'song', 'created', 'active')

admin.site.register(Comment, CommentAdmin)


class LyricAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'slug')

admin.site.register(Lyric, LyricAdmin)


