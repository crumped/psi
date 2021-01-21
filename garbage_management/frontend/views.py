from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import requests
from .forms import *


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
        return render(request, 'kierownik-przewozu-smieci/users/users.html', {'data': data["results"]})


def places_kps(request):
    if request.method == 'GET':
        url = merge_url(request, "api/places")
        headers_dict = {"Authorization": "Token " + request.session['token']}
        response = requests.get(url, headers=headers_dict)
        data = response.json()
        return render(request, 'kierownik-przewozu-smieci/places/places.html', {'data': data["results"]})


def add_user_kps(request):
    if request.method == 'GET':
        form = AddUserForm()
        return render(request, 'kierownik-przewozu-smieci/users/adduser.html', {'form': form})
    else:
        form = AddUserForm(request.POST)
        if form.is_valid():
            url = merge_url(request, "api/users")
            headers_dict = {"Authorization": "Token " + request.session['token']}
            my_obj = {"username": form.data['username'], "first_name": form.data['firstname'],"last_name": form.data['lastname'],"groups": form.data['group'],"password": form.data['password']}
            response = requests.post(url, data=my_obj, headers=headers_dict)
            data = response.json()
            if response.status_code == 404 or response.status_code == 400:
                form = AddUserForm()
                return render(request, 'kierownik-przewozu-smieci/users/adduser.html', {'form': form})
            return redirect("/kierownik-przewozu-smieci/uzytkownicy")


def delete_user_kps(request, id):
    if request.method == "POST":
        url = merge_url(request, "api/users/{id}".format(id=id))
        headers_dict = {"Authorization": "Token " + request.session['token']}
        response = requests.delete(url, headers=headers_dict)
        return redirect('/kierownik-przewozu-smieci/uzytkownicy')


def cars_kps(request):
    if request.method == 'GET':
        url = merge_url(request, "api/cars")
        headers_dict = {"Authorization": "Token " + request.session['token']}
        response = requests.get(url, headers=headers_dict)
        data = response.json()
        return render(request, 'kierownik-przewozu-smieci/cars/cars.html', {'data': data["results"]})


def add_cars_kps(request):
    if request.method == 'GET':
        form = CarsForm()
        return render(request, 'kierownik-przewozu-smieci/cars/addcars.html', {'form': form})
    else:
        form = CarsForm(request.POST)
        if form.is_valid():
            url = merge_url(request, "api/cars")
            headers_dict = {"Authorization": "Token " + request.session['token']}
            my_obj = {"number_plate": form.data['number_plate'],
                      "mileage": form.data['mileage'],
                      "date_oil": form.data['date_oil'],
                      "mileage_oil": form.data['mileage_oil'],
                      "car_type": form.data['car_type']
                      }
            response = requests.post(url, data=my_obj, headers=headers_dict)
            data = response.json()
            if response.status_code == 404 or response.status_code == 400:
                form = CarsForm()
                return render(request, 'kierownik-przewozu-smieci/cars/addcars.html', {'form': form})
            return redirect("/kierownik-przewozu-smieci/pojazdy")

def tracks_kps(request):
    if request.method == 'GET':
        url = merge_url(request, "api/tracks")
        headers_dict = {"Authorization": "Token " + request.session['token']}
        response = requests.get(url, headers=headers_dict)
        data = response.json()
        return render(request, 'kierownik-przewozu-smieci/tracks/tracks.html', {'data': data["results"]})


def add_track_kps(request):
    if request.method == 'GET':
        form = TrackForm()
        return render(request, 'kierownik-przewozu-smieci/tracks/addtrack.html', {'form': form})
    else:
        form = TrackForm(request.POST)
        if form.is_valid():
            url = merge_url(request, "api/tracks")
            headers_dict = {"Authorization": "Token " + request.session['token']}
            my_obj = {
                "car": form.data['car'],
                "garbage_dump": form.data['garbage_dump'],
                "start_date": form.data['start_date'],
                "is_done": form.data['is_done'],
                "driver": form.data['driver']
            }
            response = requests.post(url, data=my_obj, headers=headers_dict)
            data = response.json()
            if response.status_code == 404 or response.status_code == 400:
                form = TrackForm()
                return render(request, 'kierownik-przewozu-smieci/tracks/addtrack.html', {'form': form})
            return redirect("/kierownik-przewozu-smieci/trasy")


def edit_track_kps(request, id):
    if request.method == 'GET':
        url = merge_url(request, "api/tracks/{id}".format(id=id))
        headers_dict = {"Authorization": "Token " + request.session['token']}
        response = requests.get(url, headers=headers_dict)
        form = TrackForm(response.json())

        url = merge_url(request, "api/stops?track={id}".format(id=id))
        headers_dict = {"Authorization": "Token " + request.session['token']}
        response = requests.get(url, headers=headers_dict)
        print(response.json())
        data = response.json()
        return render(request, 'kierownik-przewozu-smieci/tracks/edittrack.html', {'form': form, 'stops': data['results'], 'track_id': id})
    else:
        form = TrackForm(request.POST)
        if form.is_valid():
            url = merge_url(request, "api/tracks/{id}".format(id=id))
            headers_dict = {"Authorization": "Token " + request.session['token']}
            my_obj = {
                "car": form.data['car'],
                "garbage_dump": form.data['garbage_dump'],
                "start_date": form.data['start_date'],
                "is_done": form.data['is_done'],
                "driver": form.data['driver']
            }
            response = requests.put(url, data=my_obj, headers=headers_dict)
            if response.status_code == 404 or response.status_code == 400:
                url = merge_url(request, "api/tracks/{id}".format(id=id))
                headers_dict = {"Authorization": "Token " + request.session['token']}
                response = requests.get(url, headers=headers_dict)
                form = TrackForm(response.json())

                url = merge_url(request, "api/stops?track={id}".format(id=id))
                headers_dict = {"Authorization": "Token " + request.session['token']}
                response = requests.get(url, headers=headers_dict)
                print(response.json())
                data = response.json()
                return render(request, 'kierownik-przewozu-smieci/tracks/edittrack.html', {'form': form, 'stops': data['results'], 'track_id': id})
            return redirect("/kierownik-przewozu-smieci/trasy")


def add_stop_kps(request, id):
    if request.method == 'GET':
        form = StopsForm()
        return render(request, 'kierownik-przewozu-smieci/stops/addstop.html', {'form': form})
    else:
        form = StopsForm(request.POST)
        if form.is_valid():
            url = merge_url(request, "api/stops")
            headers_dict = {"Authorization": "Token " + request.session['token']}
            my_obj = {
                "bin": form.data['bin'],
                "stop_number": form.data['stop_number'],
                "track": {id}
            }
            response = requests.post(url, data=my_obj, headers=headers_dict)
            data = response.json()
            if response.status_code == 404 or response.status_code == 400:
                form = StopsForm()
                return render(request, 'kierownik-przewozu-smieci/tracks/addstop.html', {'form': form})
            return redirect("/kierownik-przewozu-smieci/trasy/edytuj/{id}".format(id=id))


def edit_stop_kps(request, id, id2):
    if request.method == 'GET':
        url = merge_url(request, "api/stops/{id}".format(id=id))
        headers_dict = {"Authorization": "Token " + request.session['token']}
        response = requests.get(url, headers=headers_dict)
        form = StopsForm(response.json())
        return render(request, 'kierownik-przewozu-smieci/stops/editstop.html', {'form': form})
    else:
        form = StopsForm(request.POST)
        if form.is_valid():
            url = merge_url(request, "api/stops/{id}".format(id=id))
            headers_dict = {"Authorization": "Token " + request.session['token']}
            my_obj = {
                "bin": form.data['bin'],
                "stop_number": form.data['stop_number']
            }
            response = requests.put(url, data=my_obj, headers=headers_dict)
            if response.status_code == 404 or response.status_code == 400:
                url = merge_url(request, "api/stops/{id}".format(id=id))
                headers_dict = {"Authorization": "Token " + request.session['token']}
                response = requests.get(url, headers=headers_dict)
                form = StopsForm(response.json())
                return render(request, 'kierownik-przewozu-smieci/stops/editstop.html', {'form': form})
            return redirect("/kierownik-przewozu-smieci/trasy/edytuj/{id}".format(id=id2))


def edit_car_kps(request, id):
    if request.method == 'GET':
        url = merge_url(request, "api/cars/{id}".format(id=id))
        headers_dict = {"Authorization": "Token " + request.session['token']}
        response = requests.get(url, headers=headers_dict)
        form = CarsForm(response.json())
        return render(request, 'kierownik-przewozu-smieci/cars/edit.html', {'form': form, 'car_id': id})
    else:
        form = CarsForm(request.POST)
        if form.is_valid():
            url = merge_url(request, "api/cars/{id}".format(id=id))
            headers_dict = {"Authorization": "Token " + request.session['token']}
            my_obj = {
                      "number_plate": form.data['number_plate'],
                      "mileage": form.data['mileage'],
                      "date_oil": form.data['date_oil'],
                      "mileage_oil": form.data['mileage_oil'],
                      "car_type": form.data['car_type']
            }
            response = requests.put(url, data=my_obj, headers=headers_dict)
            if response.status_code == 404 or response.status_code == 400:
                url = merge_url(request, "api/cars/{id}".format(id=id))
                headers_dict = {"Authorization": "Token " + request.session['token']}
                response = requests.get(url, headers=headers_dict)
                form = CarsForm(response.json())
                return render(request, 'kierownik-przewozu-smieci/cars/edit.html',
                              {'form': form, 'car_id': id})
            return redirect("/kierownik-przewozu-smieci/pojazdy")


def delete_car_kps(request, id):
    if request.method == "POST":
        url = merge_url(request, "api/cars/{id}".format(id=id))
        headers_dict = {"Authorization": "Token " + request.session['token']}
        response = requests.delete(url, headers=headers_dict)
        return redirect('/kierownik-przewozu-smieci/pojazdy')


def trash_bin_kps(request):
    if request.method == 'GET':
        url = merge_url(request, "api/trash-bins")
        headers_dict = {"Authorization": "Token " + request.session['token']}
        response = requests.get(url, headers=headers_dict)
        data = response.json()
        return render(request, 'kierownik-przewozu-smieci/trash_bins/trash_bins.html', {'data': data["results"]})


def add_trash_bin_kps(request):
    if request.method == 'GET':
        form = TrashBinForm()
        return render(request, 'kierownik-przewozu-smieci/trash_bins/add.html', {'form': form})
    else:
        form = TrashBinForm(request.POST)
        if form.is_valid():
            url = merge_url(request, "api/trash-bins")
            headers_dict = {"Authorization": "Token " + request.session['token']}
            my_obj = {"bin_capacity": form.data['bin_capacity'],
                      "bin_type": form.data['bin_type'],
                      "address": form.data['address'],
                      "bin_size": form.data['bin_size']
                      }
            response = requests.post(url, data=my_obj, headers=headers_dict)
            data = response.json()
            if response.status_code == 404 or response.status_code == 400:
                form = CarsForm()
                return render(request, 'kierownik-przewozu-smieci/trash_bins/trash_bins.html', {'form': form})
            return redirect("/kierownik-przewozu-smieci/pojemniki")


def delete_trash_bin_kps(request, id):
    if request.method == "POST":
        url = merge_url(request, "api/trash-bins/{id}".format(id=id))
        headers_dict = {"Authorization": "Token " + request.session['token']}
        response = requests.delete(url, headers=headers_dict)
        return redirect('/kierownik-przewozu-smieci/pojemniki')


def edit_trash_bin_kps(request, id):
    if request.method == 'GET':
        url = merge_url(request, "api/trash-bins/{id}".format(id=id))
        headers_dict = {"Authorization": "Token " + request.session['token']}
        response = requests.get(url, headers=headers_dict)
        form = TrashBinForm(response.json())
        return render(request, 'kierownik-przewozu-smieci/trash_bins/edit.html', {'form': form, 'trash-bins_id': id})
    else:
        form = TrashBinForm(request.POST)
        if form.is_valid():
            url = merge_url(request, "api/trash-bins/{id}".format(id=id))
            headers_dict = {"Authorization": "Token " + request.session['token']}
            my_obj = {
                      "bin_capacity": form.data['bin_capacity'],
                      "bin_type": form.data['bin_type'],
                      "address": form.data['address'],
                      "bin_size": form.data['bin_size']
            }
            response = requests.put(url, data=my_obj, headers=headers_dict)
            if response.status_code == 404 or response.status_code == 400:
                url = merge_url(request, "api/trash-bins/{id}".format(id=id))
                headers_dict = {"Authorization": "Token " + request.session['token']}
                response = requests.get(url, headers=headers_dict)
                form = TrashBinForm(response.json())
                return render(request, 'kierownik-przewozu-smieci/trash_bins/edit.html',
                              {'form': form, 'trash-bins_id': id})
            return redirect("/kierownik-przewozu-smieci/pojemniki")
