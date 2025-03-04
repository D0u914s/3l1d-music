from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Song
from .forms import SongForm


def upload_song(request):
    """
    View para upload de novas músicas.
    """
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Música enviada com sucesso!')
            return redirect('song_list')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = SongForm()
    
    return render(request, 'music_stream/upload.html', {
        'form': form,
        'title': 'Enviar Nova Música'
    })


def song_list(request):
    """
    View para listar todas as músicas.
    """
    songs = Song.objects.all()
    return render(request, 'music_stream/song_list.html', {
        'songs': songs,
        'title': 'Biblioteca de Músicas'
    })


def song_detail(request, pk):
    """
    View para exibir detalhes de uma música específica.
    """
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'music_stream/song_detail.html', {
        'song': song,
        'title': f'{song.title} - {song.artist}'
    })
