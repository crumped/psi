from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import requests
from .forms import LoginForm, AddUserForm


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


def merge_url(request, path):
    domain = request.META['HTTP_HOST']
    url = f'http://{domain}/{path}'
    return url


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            url = merge_url(request, "api-token-auth")
            my_obj = {'username': form.data['login'], 'password': form.data['password']}
            response = requests.post(url, data=my_obj)
            data = response.json()
            if response.status_code == 404 or response.status_code == 400:
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


def logout(request):
    if request.method == "GET":
        del request.session['token']
        return redirect('/login')


def index_kps(request):
    if request.method == 'GET':
        return render(request, 'kierownik-przewozu-smieci/index.html')


def users_kps(request):
    if request.method == 'GET':
        url = merge_url(request, "api/users")
        headers_dict = {"Authorization": "Token " + request.session['token']}
        response = requests.get(url, headers=headers_dict)
        data = response.json()
        print(data)
        return render(request, 'kierownik-przewozu-smieci/users.html', {'data': data["results"]})


def places_kps(request):
    if request.method == 'GET':
        url = merge_url(request, "api/places")
        headers_dict = {"Authorization": "Token " + request.session['token']}
        response = requests.get(url, headers=headers_dict)
        data = response.json()
        print(data)
        return render(request, 'kierownik-przewozu-smieci/places.html', {'data': data["results"]})


def adduser_kps(request):
    if request.method == 'GET':
        form = AddUserForm(request.POST)
        return render(request, 'kierownik-przewozu-smieci/adduser.html', {'form': form})


def deleteuser_kps(request, id):
    if request.method == "POST":
        url = merge_url(request, "api/users/{id}".format(id=id))
        headers_dict = {"Authorization": "Token " + request.session['token']}
        response = requests.delete(url, headers=headers_dict)
        print(response)
        print(response.status_code)
        # return users_kps(request)
        return redirect('/kierownik-przewozu-smieci/uzytkownicy')
