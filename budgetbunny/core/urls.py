from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index_page, name='show_index_page'),
    path('', views.show_game_description, name="show_game_description")
]