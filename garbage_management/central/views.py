from django.http import Http404
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .permissions import HasGroupPermission
from rest_framework.response import Response
from rest_framework import status
from .models import Cars, TrashBin, GarbageDump
from .serializers import CarsSerializer, TrashBinSerializer, GarbageDumpSerializer, UserSerializer
from django.contrib.auth.models import User


def index(request):
    return render(request, 'html/main.html')


class CarDetailsView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'OPTIONS': ['__all__'],
        'GET': ['kps'],
        'POST': ['moderators', 'someMadeUpGroup'],
        'PUT': ['__all__'],
        'DELETE': ['kps'],
    }

    def get(self, request, pk, format=None):
        cars = Cars.objects.get(pk=pk)
        serializer = CarsSerializer(cars)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        cars = Cars.objects.get(pk=pk)
        serializer = CarsSerializer(cars, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cars = Cars.objects.get(pk=pk)
        cars.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarsView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'OPTIONS': ['__all__'],
        'GET': ['kps', 'members'],
        'POST': ['kps', 'someMadeUpGroup'],
        'PUT': ['__all__'],
        'DELETE': ['kps'],
    }

    def get(self, request, format=None):
        cars = Cars.objects.all()
        serializer = CarsSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class TrashBinDetailsView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kps'],
        'PUT': ['__all__'],
        'DELETE': ['kps'],
    }

    def get(self, request, pk, format=None):
        trash_bin = TrashBin.objects.get(pk=pk)
        serializer = TrashBinSerializer(trash_bin)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        trash_bin = TrashBin.objects.get(pk=pk)
        serializer = TrashBinSerializer(trash_bin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        trash_bin = TrashBin.objects.get(pk=pk)
        trash_bin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TrashBinsView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kps', 'members'],
        'POST': ['kps', 'someMadeUpGroup'],
        'PUT': ['__all__'],
        'DELETE': ['kps'],
    }

    def get(self, request, format=None):
        trash_bins = TrashBin.objects.all()
        serializer = CarsSerializer(trash_bins, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TrashBinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class GarbageDumpDetailsView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kps'],
        'PUT': ['__all__'],
        'DELETE': ['kps'],
    }

    def get(self, request, pk, format=None):
        garbage_dump = GarbageDump.objects.get(pk=pk)
        serializer = GarbageDumpSerializer(garbage_dump)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        garbage_dump = GarbageDump.objects.get(pk=pk)
        serializer = GarbageDumpSerializer(garbage_dump, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        garbage_dump = GarbageDump.objects.get(pk=pk)
        garbage_dump.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GarbageDumpView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kps', 'members'],
        'POST': ['kps', 'someMadeUpGroup'],
        'PUT': ['__all__'],
        'DELETE': ['kps'],
    }

    def get(self, request, format=None):
        garbage_dumps = GarbageDump.objects.all()
        serializer = CarsSerializer(garbage_dumps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = GarbageDumpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class UsersView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['szef', 'kierownik-glowny', 'kierownik-przewozu-smieci', 'kierownik-wysypiska'],
        'POST': ['kps', 'someMadeUpGroup'],
        'PUT': ['__all__'],
        'DELETE': ['kps'],
    }

    def get(self, request, format=None):

        current_user = User.objects.all().filter(username=request.user).first()
        serializer = UserSerializer(current_user)
        if 'szef' in serializer.data['groups']:
            users = User.objects.all().filter(is_superuser=False, )
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

        if 'kierownik-glowny' in serializer.data['groups']:
            exclude_array = ['szef']
            users = User.objects.all().filter(is_superuser=False).exclude(groups__name__in=exclude_array)
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

        if 'kierownik-przewozu-smieci' in serializer.data['groups']:
            include_array = ['kierowca-smieciarki', 'pracownicy-przewozacy-smieci']
            users = User.objects.all().filter(is_superuser=False, groups__name__in=include_array)
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

        if 'kierownik-wysypiska' in serializer.data['groups']:
            include_array = ['pracownik-wysypiska']
            users = User.objects.all().filter(is_superuser=False, groups__name__in=include_array)
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)


class UserDetailsView(APIView):
    pass
