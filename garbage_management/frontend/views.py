from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import requests
from .forms import LoginForm


def get_user_group(user_id):
    user = User.objects.get(pk=user_id)
    l1 = user.groups.values_list('name', flat=True)
    l_as_list = list(l1)
    all_groups = ['kierowca-smieciarki', 'kierownik-glowny', 'kierownik-przewozu-smieci', 'kierownik-wysypiska',
                  'ksiegowosc', 'pracownicy-przewozacy-smieci', 'pracownik-wysypiska', 'szef']
    bool_array = tuple(x in l_as_list for x in all_groups)
    group_index = None
    for index, i in enumerate(bool_array, start=0):
        if i:
            group_index = index
            break
    return all_groups[group_index]


def merge_url(request):
    domain = request.META['HTTP_HOST']
    url = f'http://{domain}/api-token-auth'
    return url


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            url = merge_url(request)
            my_obj = {'username': form.data['login'], 'password': form.data['password']}
            response = requests.post(url, data=my_obj)
            data = response.json()
            if response.status_code == (404 or 400):
                form = LoginForm()
                return render(request, 'login.html', {'form': form})
            group = get_user_group(data['user_id'])
            if group:
                request.session['token'] = data['token']
                return redirect(f'/{group}')
            return redirect('/login')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})