from django.db import models

# Create your models here.

class Song(models.Model):
    """
    Modelo para armazenar informações sobre músicas no sistema.
    """
    title = models.CharField(max_length=255, verbose_name='Título')
    artist = models.CharField(max_length=255, verbose_name='Artista')
    album = models.CharField(max_length=255, verbose_name='Álbum')
    mp3_file = models.FileField(upload_to='music/', verbose_name='Arquivo MP3')
    cover_image = models.ImageField(upload_to='covers/', verbose_name='Imagem de Capa')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    
    class Meta:
        verbose_name = 'Música'
        verbose_name_plural = 'Músicas'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.artist}"
