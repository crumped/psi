from django.urls import path
from .views import login

urlpatterns = [
    path('login', login, name="login"),
    path('kierowca-smieciarki', login, name="login"),
    path('kierownik-glowny', login, name="login"),
    path('kierownik-przewozu-smieci', login, name="login"),
    path('kierownik-wysypiska', login, name="login"),
    path('ksiegowosc', login, name="login"),
    path('pracownicy-przewozacy-smieci', login, name="login"),
    path('pracownik-wysypiska', login, name="login"),
]
