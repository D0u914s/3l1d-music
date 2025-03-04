import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_stream_project.settings')
django.setup()

from music_stream.models import Song

songs = Song.objects.all()
print("\nMúsicas no banco de dados:")
print("-" * 50)
for song in songs:
    print(f"\nTítulo: {song.title}")
    print(f"Artista: {song.artist}")
    print(f"Álbum: {song.album}")
    print(f"Arquivo MP3: {song.mp3_file}")
    print(f"Imagem de Capa: {song.cover_image}")
    print(f"Data de Criação: {song.created_at}")
    print("-" * 50) 