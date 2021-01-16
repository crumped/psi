from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())