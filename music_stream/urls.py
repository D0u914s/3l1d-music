from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),  # Página inicial: lista de músicas
    path('upload/', views.upload_song, name='upload'),  # Upload de músicas
    path('song/<int:pk>/', views.song_detail, name='song_detail'),  # Detalhes da música
] 