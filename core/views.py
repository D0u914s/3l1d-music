from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Olá, Django está rodando com sucesso! 🚀</h1>")
