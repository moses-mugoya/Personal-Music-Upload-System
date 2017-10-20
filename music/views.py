from django.shortcuts import render, get_object_or_404
from .models import DailyQuotes, BibleQuotes, Song, Lyric
from .forms import CommentForm
from django.contrib import messages


def index(request):
    daily = DailyQuotes.objects.all()
    bible = BibleQuotes.objects.all()
    song = Song.objects.all()
    lyrics = Lyric.objects.all()

    return render(request, 'music/index.html', {'daily': daily, 'bible': bible, 'song': song, 'lyrics': lyrics})


def song_detail(request, year, month, day, song):
    song = get_object_or_404(Song, slug=song,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day
                             )

    comments = song.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.song = song
            new_comment.save()
            messages.success(request, 'Your comment has been successfully added')
        else:
            messages.error(request, 'There was an error trying to add your comment')
    else:
        comment_form = CommentForm()

    return render(request, 'music/song_detail.html', {'songs': song, 'comment_form': comment_form, 'comments': comments})


def song_lyrics(request, year, month, day, lyric):
    lyric = get_object_or_404(Lyric, slug=lyric,
                              publish__year=year,
                              publish__month=month,
                              publish__day=day
                              )
    return render(request, 'music/song_lyrics.html', {'lyric': lyric})


def breaking_free(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'music/breaking_free.html', {'song': song})


def god_like(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'music/god_like.html', {'song': song})
