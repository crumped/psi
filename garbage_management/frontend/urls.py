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
    path('kierownik-przewozu-smieci/pojazdy/dodaj', add_cars_kps, name="add car kps"),

    path('kierownik-przewozu-smieci/miejscaRozladunku', places_kps, name="places kps"),

    path('kierownik-przewozu-smieci/trasy', tracks_kps, name="tracks kps"),
    path('kierownik-przewozu-smieci/trasy/dodaj', add_track_kps, name="add track kps"),
    path('kierownik-przewozu-smieci/trasy/edytuj/<int:id>', edit_track_kps, name="edit track kps"),

    path('kierownik-przewozu-smieci/przystanki/dodaj/<int:id>', add_stop_kps, name="add stop kps"),
    path('kierownik-przewozu-smieci/przystanki/edytuj/<int:id>/<int:id2>', edit_stop_kps, name="edit stop kps"),

    path('kierownik-przewozu-smieci/uzytkownicy', users_kps, name="users kps"),
    path('kierownik-przewozu-smieci/uzytkownicy/dodaj', add_user_kps, name="add user kps"),
    path('kierownik-przewozu-smieci/uzytkownicy/usun/<int:id>', delete_user_kps, name="delete user kps"),

    path('kierownik-wysypiska', login, name="login"),

    path('ksiegowosc', login, name="login"),

    path('pracownicy-przewozacy-smieci', login, name="login"),

    path('pracownik-wysypiska', login, name="login"),
]
