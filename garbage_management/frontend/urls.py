from django.urls import path
from .views import *

urlpatterns = [
    path('login', login, name="login"),
    path('kierowca-smieciarki', login, name="login"),
    path('kierownik-glowny', login, name="login"),
    path('kierownik-przewozu-smieci', index_kps, name="index kps"),
    path('kierownik-przewozu-smieci/uzytkownicy', users_kps, name="users kps"),
    path('kierownik-wysypiska', login, name="login"),
    path('ksiegowosc', login, name="login"),
    path('pracownicy-przewozacy-smieci', login, name="login"),
    path('pracownik-wysypiska', login, name="login"),
]
