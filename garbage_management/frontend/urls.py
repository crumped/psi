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
    path('kierownik-przewozu-smieci/pojazdy/edytuj/<int:id>', edit_car_kps, name="edit car kps"),
    path('kierownik-przewozu-smieci/pojazdy/usun/<int:id>', delete_car_kps, name="delete car kps"),

    path('kierownik-przewozu-smieci/miejscaRozladunku', places_kps, name="places kps"),

    path('kierownik-przewozu-smieci/trasy', tracks_kps, name="tracks kps"),
    path('kierownik-przewozu-smieci/trasy/dodaj', add_track_kps, name="add track kps"),
    path('kierownik-przewozu-smieci/trasy/edytuj/<int:id>', edit_track_kps, name="edit track kps"),

    path('kierownik-przewozu-smieci/przystanki/dodaj/<int:id>', add_stop_kps, name="add stop kps"),
    path('kierownik-przewozu-smieci/przystanki/edytuj/<int:id>/<int:id2>', edit_stop_kps, name="edit stop kps"),

    path('kierownik-przewozu-smieci/grafik', schedule_kps, name="schedule kps"),
    path('kierownik-przewozu-smieci/grafik/dodaj', add_schedule_kps, name="add schedule kps"),
    path('kierownik-przewozu-smieci/grafik/edytuj/<int:id>', edit_schedule_kps, name="edit user kps"),
    path('kierownik-przewozu-smieci/grafik/usun/<int:id>', delete_schedule_kps, name="delete user kps"),

    path('kierownik-przewozu-smieci/uzytkownicy', users_kps, name="users kps"),
    path('kierownik-przewozu-smieci/uzytkownicy/dodaj', add_user_kps, name="add user kps"),
    path('kierownik-przewozu-smieci/uzytkownicy/usun/<int:id>', delete_user_kps, name="delete user kps"),
    path('kierownik-przewozu-smieci/uzytkownicy/edytuj/<int:id>', edit_user_kps, name="edit user kps"),

    path('kierownik-przewozu-smieci/pojemniki', trash_bin_kps, name="trash bin kps"),
    path('kierownik-przewozu-smieci/pojemniki/dodaj', add_trash_bin_kps, name="trash bin kps"),
    path('kierownik-przewozu-smieci/pojemniki/usun/<int:id>', delete_trash_bin_kps, name="delete car kps"),
    path('kierownik-przewozu-smieci/pojemniki/edytuj/<int:id>', edit_trash_bin_kps, name="delete car kps"),

    path('kierownik-wysypiska', login, name="login"),

    path('ksiegowosc', login, name="login"),

    path('pracownicy-przewozacy-smieci', login, name="login"),

    path('pracownik-wysypiska', login, name="login"),
]
