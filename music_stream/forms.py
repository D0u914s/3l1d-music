from django import forms
from .models import Song


class SongForm(forms.ModelForm):
    """
    Formulário para upload de novas músicas.
    """
    class Meta:
        model = Song
        fields = ['title', 'artist', 'album', 'mp3_file', 'cover_image']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da música'}),
            'artist': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do artista'}),
            'album': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do álbum'}),
            'mp3_file': forms.FileInput(attrs={'class': 'form-control'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
        } 