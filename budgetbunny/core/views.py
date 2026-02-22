from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CardInfo

# Create your views here.

def show_index_page(request):
    return render(request, "core/index.html")

def show_game_description(request):
    return render(request, "core/game-description.html")

def choose_character(request):
    if request.method == "POST":
        egg = request.POST.get("egg")
        request.session["egg_choice"] = egg
        return redirect("card_input")
    
    return render(request, "core/choose-character.html")

def card_input(request):
    if request.method == "POST":
        formset = CardInfo(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    form.save() # save each card to Neon database
            return render(request, "success.html")
    else:
        formset = CardInfo()
    return render(request, "card_form.html", {"formset": formset})
