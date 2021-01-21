from django import forms


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
    lastname = forms.CharField(label="Nazwisko", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                               'placeholder': 'Nazwisko'}))
    adress = forms.CharField(label="Adres", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                          'placeholder': 'Adres'}))
    CHOICES = (('kierowca-smieciarki', 'Kierowca Śmieciarki'), ('pracownicy-przewozacy-smieci', 'Pracownik Śmieciarki'),)
    group = forms.ChoiceField(label="Stanowisko", choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
