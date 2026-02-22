from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CardInfo

# Create your views here.

# Show the index page
def show_index_page(request):
    return render(request, "core/index.html")

# Show the game description page (with the statsitic)
def show_game_description(request):
    return render(request, "core/game-description.html")

# Receive character selection input
def choose_character(request):
    if request.method == "POST":
        egg = request.POST.get("egg")
        request.session["egg_choice"] = egg
        return redirect("card_input")
    
    return render(request, "core/choose-character.html")

# Still working on this

# Show main
def show_main(request):
    return render(request, 'core/main.html')

def show_cscreen(request):
    return render(request, "core/cscreen.html")

def show_shop(request):
    return render(request, "core/shop.html")
