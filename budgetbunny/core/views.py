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
        return redirect("card_form")
    
    return render(request, "core/choose-character.html")

# Show the card form with the chosen egg
def show_card_form(request):
    egg = request.session.get("egg_choice")
    return render(request, "core/card_form.html", {"egg": egg})

# Still working on this
# # Receive user input
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
    return render(request, "core/choose-character.html")

# Show main
def show_main(request):
    return render(request, 'core/main.html')
