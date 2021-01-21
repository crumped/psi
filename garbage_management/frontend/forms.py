import datetime

from django import forms
from central.models import *
from django.contrib.auth.models import User
# from garbage_management.central.models import *


class LoginForm(forms.Form):
    login = forms.CharField(label='Nazwa użytkownika', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Nazwa użytkownika'}))
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'Hasło'}))


class AddUserForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Nazwa użytkownika'}))
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'Hasło'}))
    firstname = forms.CharField(label="Imię", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                            'placeholder': 'Imię'}))
    lastname = forms.CharField(label="Nazwisko", max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Nazwisko'}))
    adress = forms.CharField(label="Adres", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                          'placeholder': 'Adres'}))
    CHOICES = (
        ('kierowca-smieciarki', 'Kierowca Śmieciarki'), ('pracownicy-przewozacy-smieci', 'Pracownik Śmieciarki')
    )
    group = forms.ChoiceField(label="Stanowisko", choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))


class TrackForm(forms.Form):
    car = forms.ModelChoiceField(label='Samochód', queryset=Cars.objects.all(), to_field_name="number_plate", initial=0, widget=forms.Select(
        attrs={'class': 'form-select'}))
    garbage_dump = forms.ModelChoiceField(label='Miejsce rozładunku', queryset=GarbageDump.objects.all(), to_field_name="address", initial=0,
                                          widget=forms.Select(attrs={'class': 'form-select'}))
    CHOICES = (('0', 'Nie'), ('1', 'Tak'),)
    is_done = forms.ChoiceField(label='Czy zrealizowane', choices=CHOICES, widget=forms.Select(
        attrs={'class': 'form-select'}))
    driver = forms.ModelChoiceField(label='Kierowca', queryset=User.objects.all()
                                    .filter(groups__name='kierowca-smieciarki'), to_field_name="username", initial=0,
                                    widget=forms.Select(attrs={'class': 'form-select'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control', 'placeholder': 'Dzień rozpoczęcia', 'value': datetime.date.today}))


class StopsForm(forms.Form):
    bin = forms.ModelChoiceField(label='Pojemnik na śmieci', queryset=TrashBin.objects.all(), to_field_name="address", initial=0, widget=forms.Select(
        attrs={'class': 'form-select'}))
    stop_number = forms.IntegerField(label='Numer przystanku', widget=forms.NumberInput(attrs={'class': 'form-control'}))


