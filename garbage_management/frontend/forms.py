from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class AddUserForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    firstname = forms.CharField(label="Imię", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(label="Nazwisko",max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    adress = forms.CharField(label="Adres",max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    CHOICES = (('kierowca-smieciarki', 'Kierowca Śmieciarki'), ('pracownik-przewazacy-smieci', 'Pracownik Śmieciarki'),)
    group = forms.ChoiceField(label="Stanowisko",choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))


