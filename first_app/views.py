from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import *
from first_app import forms
from django.db.models import Avg
# Create your views here.


def index(request):
    musician_list = Musician.objects.order_by('first_name')
    context = {'title': 'This is Homepage', 'musician_list': musician_list}
    return render(request, 'first_app/index.html', context=context)


def album_list(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    all_album = Album.objects.filter(artist=artist_id).order_by('name', 'release_date')
    artist_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('rating'))
    context = {'title': 'Album List', 'artist_info': artist_info, 'all_album': all_album, 'artist_rating': artist_rating}
    return render(request, 'first_app/album_list.html', context=context)


def add_musician(request):
    form = forms.MusicianForm()
    if request.method == "POST":
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    context = {'title': 'Add New Musician', 'musician_form': form, }
    return render(request, 'first_app/musician_form.html', context=context)


def add_album(request):
    form = forms.AlbumForm
    if request.method == "POST":
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    context = {'title': 'Add New Album', 'album_form': form}
    return render(request, 'first_app/album_form.html', context=context)


def update_artist(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)
    context = {}
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=artist_info)
        if form.is_valid():
            form.save(commit=True)
            context.update({'success': "Successfully Updated!"})
            # return album_list(request, artist_id)
    context.update({'update_form': form})
    return render(request, 'first_app/update_artist.html', context=context)


def update_album(request, album_id):
    album_info = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)
    context = {}
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album_info)
        if form.is_valid():
            form.save(commit=True)
            context.update({'success': "Successfully Updated!"})
            # return album_list(request, artist_id)
    context.update({'update_form': form})
    return render(request, 'first_app/update_album.html', context=context)


def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id).delete()

    context = {'delete_message': "Album Deleted Successfully!"}
    return render(request, 'first_app/delete.html', context=context)


def delete_artist(request, artist_id):
    artist = Musician.objects.get(pk=artist_id).delete()

    context = {'delete_message': "Artist Deleted Successfully!"}
    return render(request, 'first_app/delete.html', context=context)