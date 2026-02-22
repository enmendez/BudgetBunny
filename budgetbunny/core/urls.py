from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index_page, name='show_index_page'),
    path('game/', views.show_game_description, name='show_game_description'),
    path('choose-character/', views.choose_character, name='choose_character'),
    path('main/', views.show_main, name='show_main'),
    path('cscreen/', views.show_cscreen, name='show_cscreen'),
    path('shop/', views.show_shop, name="show_shop")
]