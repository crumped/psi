from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),

    path('login', login, name="login"),
    path('logout', logout, name="logout"),

    path('kierowca-smieciarki', login, name="login"),

    path('kierownik-glowny', login, name="login"),

    path('kierownik-przewozu-smieci', index_kps, name="index kps"),
    path('kierownik-przewozu-smieci/pojazdy', cars_kps, name="cars kps"),
    path('kierownik-przewozu-smieci/uzytkownicy', users_kps, name="users kps"),
    path('kierownik-przewozu-smieci/pojazdy/dodaj', addcars_kps, name="cars kps"),
    path('kierownik-przewozu-smieci/miejscaRozladunku', places_kps, name="places kps"),
    path('kierownik-przewozu-smieci/uzytkownicy/dodaj', adduser_kps, name="adduser kps"),
    path('kierownik-przewozu-smieci/uzytkownicy/usun/<int:id>', deleteuser_kps, name="deleteuser kps"),

    path('kierownik-wysypiska', login, name="login"),

    path('ksiegowosc', login, name="login"),

    path('pracownicy-przewozacy-smieci', login, name="login"),

    path('pracownik-wysypiska', login, name="login"),
]
