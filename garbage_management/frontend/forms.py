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
    first_name = forms.CharField(label="Imię", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                            'placeholder': 'Imię'}))
    last_name = forms.CharField(label="Nazwisko", max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Nazwisko'}))
    email = forms.CharField(label="Email", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                          'placeholder': 'Email'}))
    CHOICES = (
        ('kierowca-smieciarki', 'Kierowca Śmieciarki'), ('pracownicy-przewozacy-smieci', 'Pracownik Śmieciarki')
    )
    groups = forms.ChoiceField(label="Stanowisko", choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))


class CarsForm(forms.Form):
    number_plate = forms.CharField(label="Numer rejestracyjny", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                          'placeholder': 'Numer rejestracyjny'}))
    mileage = forms.CharField(label="Przebieg", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                          'placeholder': 'Przebieg'}))
    date_oil = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control', 'placeholder': 'Data zmiany oleju', 'value': datetime.date.today}))
    mileage_oil = forms.CharField(label="Ilość kilometrów do zrobienia", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                          'placeholder': 'Ilość kilometrów do zrobienia'}))
    car_type = forms.ModelChoiceField(label='Rodzaj samochodu', queryset=CarType.objects.all(), to_field_name="type", initial=0, widget=forms.Select(
        attrs={'class': 'form-select'}))


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


class ScheduleForm(forms.Form):
    include_array = ['kierowca-smieciarki', 'pracownicy-przewozacy-smieci']
    user = forms.ModelChoiceField(label='Pracownik', queryset=User.objects.all()
                                    .filter(groups__name__in=include_array), to_field_name="username", initial=0,
                                    widget=forms.Select(attrs={'class': 'form-select'}))
    day = forms.DateField(label='Dzień pracy', widget=forms.DateInput(attrs={
        'class': 'form-control', 'placeholder': 'Dzień pracy', 'value': datetime.date.today}))
    CHOICES = (('Noc', 'Noc'), ('Dzień', 'Dzień'), ('Ranek', 'Ranek'), ('Wieczór', 'Wieczór'))
    work_type = forms.ChoiceField(label='Typ zmiany', choices=CHOICES, widget=forms.Select(
        attrs={'class': 'form-select'}))


class KeysForm(forms.Form):
    driver = forms.ModelChoiceField(label='Kierowca', queryset=User.objects.all()
                                    .filter(groups__name='kierowca-smieciarki'), to_field_name="username", initial=0,
                                    widget=forms.Select(attrs={'class': 'form-select'}))
    supervisor = forms.ModelChoiceField(label='Nadzorca', queryset=User.objects.all() , to_field_name="username",
                                        initial=0, widget=forms.Select(attrs={'class': 'form-select'}))
    car = forms.ModelChoiceField(label='Samochód', queryset=Cars.objects.all(), to_field_name="number_plate", initial=0,
                                 widget=forms.Select(attrs={'class': 'form-select'}))


