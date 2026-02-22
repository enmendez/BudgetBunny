from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def show_index_page(request):
    return render(request, "core/index.html")

def show_game_description(request):
    return render(request, "core/game-description.html")

def choose_character(request):
    return render(request, "core/choose-character.html")

def show_main(request):
    return render(request, 'core/main.html')