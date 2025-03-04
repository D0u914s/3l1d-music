from django.urls import path
from . import views  # Importamos as views do app

urlpatterns = [
    path('', views.home, name='home'),  # Criamos a rota para a página inicial
]
