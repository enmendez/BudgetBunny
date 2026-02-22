from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CardInfo, CardInfoForm

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

def card_form(request):
    egg = request.session.get("egg_choice")

    CardInfoFormSet = formset_factory(CardInfoForm, extra=1)

    if request.method == "POST":
        formset = CardInfoFormSet(request.POST)
        if formset.is_Valid():
            request.session["cards"] = formset.cleaned_Data
            return redirect("summary")
    else: formset = CardInfoFormSet

    return render(request, "core/card_form.html", {
        "formset": formset,
        "egg": egg
    })

# Show main
def show_main(request):
    return render(request, 'core/main.html')
