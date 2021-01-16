import datetime

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .permissions import HasGroupPermission
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Cars, TrashBin, GarbageDump, Track, BinTrack, Keys, Invoices, InvoicesNames, Schedule
from .serializers import CarsSerializer, TrashBinSerializer, GarbageDumpSerializer, UserSerializer,\
    UserModifySerializer, TrackSerializer, BinTrackSerializer, KeysSerializer, InvoicesSerializer, \
    InvoicesNamesSerializer, ScheduleSerializer
from django.contrib.auth.models import User
from rest_framework.reverse import reverse


def index(request):
    return render(request, 'html/main.html')


class CarList(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    name = 'car-list'
    filter_fields = ['id_cars', 'number_plate']
    search_fields = ['id_cars', 'number_plate']
    ordering = ['id_cars', 'car_type', 'date_oil', 'mileage_oil']
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['kierownik-przewozu-smieci', 'kierowca-smieciarki'],
        'POST': ['kierownik-przewozu-smieci'],
    }


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    name = 'car-detail'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['kierownik-przewozu-smieci', 'kierowca-smieciarki'],
        'PUT': ['kierownik-przewozu-smieci', 'kierowca-smieciarki'],
        'DELETE': ['kierownik-przewozu-smieci'],
    }


class TrashBinList(generics.ListCreateAPIView):
    queryset = TrashBin.objects.all()
    serializer_class = TrashBinSerializer
    name = 'trash-bin-list'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['kierownik-przewozu-smieci'],
        'POST': ['kierownik-przewozu-smieci'],
    }


class TrashBinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrashBin.objects.all()
    serializer_class = TrashBinSerializer
    name = 'trash-bin-detail'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['kierownik-przewozu-smieci'],
        'PUT': ['kierownik-przewozu-smieci'],
        'DELETE': ['kierownik-przewozu-smieci'],
    }


class GarbageDumpList(generics.ListCreateAPIView):
    queryset = GarbageDump.objects.all()
    serializer_class = GarbageDumpSerializer
    name = 'garbage-dump-list'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['kierownik-przewozu-smieci', 'kierownik-wysypiska'],
        'POST': ['kierownik-wysypiska'],
    }


class GarbageDumpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GarbageDump.objects.all()
    serializer_class = GarbageDumpSerializer
    name = 'garbage-dump-detail'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['kierownik-przewozu-smieci', 'kierownik-wysypiska'],
        'PUT': ['kierownik-wysypiska'],
        'DELETE': ['kierownik-wysypiska'],
    }


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModifySerializer
    name = 'user-list'
    filter_fields = ['username', 'first_name', 'last_name', 'email']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    ordering = ['first_name', 'last_name', 'email']
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['szef', 'kierownik-glowny', 'kierownik-przewozu-smieci', 'kierownik-wysypiska'],
        'POST': ['szef', 'kierownik-glowny', 'kierownik-przewozu-smieci', 'kierownik-wysypiska'],
    }

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserModifySerializer
        return UserSerializer

    def get_queryset(self):
        """Filter active products."""
        current_user = User.objects.all().filter(username=self.request.user).first()
        serializer = UserSerializer(current_user)
        if 'szef' in serializer.data['groups']:
            return User.objects.all().filter(is_superuser=False, )

        if 'kierownik-glowny' in serializer.data['groups']:
            exclude_array = ['szef']
            return User.objects.all().filter(is_superuser=False).exclude(groups__name__in=exclude_array)

        if 'kierownik-przewozu-smieci' in serializer.data['groups']:
            include_array = ['kierowca-smieciarki', 'pracownicy-przewozacy-smieci']
            return User.objects.all().filter(is_superuser=False, groups__name__in=include_array)

        if 'kierownik-wysypiska' in serializer.data['groups']:
            include_array = ['pracownik-wysypiska']
            return User.objects.all().filter(is_superuser=False, groups__name__in=include_array)

    def create(self, request, *args, **kwargs):
        current_user = User.objects.all().filter(username=request.user).first()
        serializer = UserSerializer(current_user)
        if 'szef' in serializer.data['groups']:
            available_groups = ['kierowca-smieciarki', 'kierownik-glowny', 'kierownik-przewozu-smieci',
                                'kierownik-wysypiska', 'ksiegowosc', 'pracownicy-przewozacy-smieci',
                                'pracownik-wysypiska', 'szef']
            serializer2 = self.get_serializer(data=request.data)
            if serializer2.is_valid():
                print(serializer2.validated_data)
                if serializer2.validated_data['groups'] not in available_groups:
                    return Response({"error": "That group is out of your permissions"},
                                    status=status.HTTP_400_BAD_REQUEST)
                serializer2.save()
                return Response(serializer2.data)
            return Response(serializer2.errors)

        if 'kierownik-glowny' in serializer.data['groups']:
            available_groups = ['kierowca-smieciarki', 'kierownik-glowny', 'kierownik-przewozu-smieci',
                                'kierownik-wysypiska', 'ksiegowosc', 'pracownicy-przewozacy-smieci',
                                'pracownik-wysypiska']
            serializer2 = self.get_serializer(data=request.data)
            if serializer2.is_valid():
                print(serializer2.validated_data)
                if serializer2.validated_data['groups'] not in available_groups:
                    return Response({"error": "That group is out of your permissions"},
                                    status=status.HTTP_400_BAD_REQUEST)
                serializer2.save()
                return Response(serializer2.data)
            return Response(serializer2.errors)

        if 'kierownik-przewozu-smieci' in serializer.data['groups']:
            available_groups = ['kierowca-smieciarki', 'pracownicy-przewozacy-smieci']
            serializer2 = self.get_serializer(data=request.data)
            if serializer2.is_valid():
                print(serializer2.validated_data)
                if serializer2.validated_data['groups'] not in available_groups:
                    return Response({"error": "That group is out of your permissions"},
                                    status=status.HTTP_400_BAD_REQUEST)
                serializer2.save()
                return Response(serializer2.data)
            return Response(serializer2.errors)

        if 'kierownik-wysypiska' in serializer.data['groups']:
            available_groups = ['pracownik-wysypiska']
            serializer2 = self.get_serializer(data=request.data)
            if serializer2.is_valid():
                print(serializer2.validated_data)
                if serializer2.validated_data['groups'] not in available_groups:
                    return Response({"error": "That group is out of your permissions"},
                                    status=status.HTTP_400_BAD_REQUEST)
                serializer2.save()
                return Response(serializer2.data)
            return Response(serializer2.errors)


class UserDetailsView(APIView):
    """
       View to list all users in the system.
       """
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['szef', 'kierownik-glowny', 'kierownik-przewozu-smieci', 'kierownik-wysypiska'],
        'PUT': ['szef', 'kierownik-glowny', 'kierownik-przewozu-smieci', 'kierownik-wysypiska'],
        'DELETE': ['szef', 'kierownik-glowny', 'kierownik-przewozu-smieci', 'kierownik-wysypiska'],
    }

    def get(self, request, pk, format=None):
        current_user = User.objects.all().filter(username=request.user).first()
        serializer = UserSerializer(current_user)
        if 'szef' in serializer.data['groups']:
            users = User.objects.get(pk=pk, is_superuser=False, )
            serializer = UserSerializer(users)
            return Response(serializer.data)

        if 'kierownik-glowny' in serializer.data['groups']:
            exclude_array = ['szef']
            users = User.objects.filter(pk=pk, is_superuser=False).exclude(groups__name__in=exclude_array).first()
            if not users:
                return Response({"error": "users doesn't exist or you don't have permissions"})
            serializer = UserSerializer(users)
            return Response(serializer.data)

        if 'kierownik-przewozu-smieci' in serializer.data['groups']:
            include_array = ['kierowca-smieciarki', 'pracownicy-przewozacy-smieci']
            users = User.objects.filter(pk=pk, is_superuser=False, groups__name__in=include_array).first()
            if not users:
                return Response({"error": "users doesn't exist or you don't have permissions"})
            serializer = UserSerializer(users)
            return Response(serializer.data)

        if 'kierownik-wysypiska' in serializer.data['groups']:
            include_array = ['pracownik-wysypiska']
            users = User.objects.filter(pk=pk, is_superuser=False, groups__name__in=include_array).first()
            if not users:
                return Response({"error": "users doesn't exist or you don't have permissions"})
            serializer = UserSerializer(users)
            return Response(serializer.data)

    def put(self, request, pk, format=None):
        current_user = User.objects.all().filter(username=request.user).first()
        serializer = UserSerializer(current_user)
        if 'szef' in serializer.data['groups']:
            users = User.objects.get(pk=pk, is_superuser=False, )
            serializer = UserSerializer(users, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if 'kierownik-glowny' in serializer.data['groups']:
            exclude_array = ['szef']
            users = User.objects.filter(pk=pk, is_superuser=False).exclude(groups__name__in=exclude_array).first()
            if not users:
                return Response({"error": "users doesn't exist or you don't have permissions"})
            serializer = UserSerializer(users, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if 'kierownik-przewozu-smieci' in serializer.data['groups']:
            include_array = ['kierowca-smieciarki', 'pracownicy-przewozacy-smieci']
            users = User.objects.filter(pk=pk, is_superuser=False, groups__name__in=include_array).first()
            if not users:
                return Response({"error": "users doesn't exist or you don't have permissions"})
            serializer = UserSerializer(users, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if 'kierownik-wysypiska' in serializer.data['groups']:
            include_array = ['pracownik-wysypiska']
            users = User.objects.filter(pk=pk, is_superuser=False, groups__name__in=include_array).first()
            if not users:
                return Response({"error": "users doesn't exist or you don't have permissions"})
            serializer = UserSerializer(users, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        current_user = User.objects.all().filter(username=request.user).first()
        serializer = UserSerializer(current_user)
        if 'szef' in serializer.data['groups']:
            users = User.objects.get(pk=pk, is_superuser=False, )
            users.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        if 'kierownik-glowny' in serializer.data['groups']:
            exclude_array = ['szef']
            users = User.objects.filter(pk=pk, is_superuser=False).exclude(groups__name__in=exclude_array).first()
            if not users:
                return Response({"error": "users doesn't exist or you don't have permissions"})
            users.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        if 'kierownik-przewozu-smieci' in serializer.data['groups']:
            include_array = ['kierowca-smieciarki', 'pracownicy-przewozacy-smieci']
            users = User.objects.filter(pk=pk, is_superuser=False, groups__name__in=include_array).first()
            if not users:
                return Response({"error": "users doesn't exist or you don't have permissions"})
            users.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        if 'kierownik-wysypiska' in serializer.data['groups']:
            include_array = ['pracownik-wysypiska']
            users = User.objects.filter(pk=pk, is_superuser=False, groups__name__in=include_array).first()
            if not users:
                return Response({"error": "users doesn't exist or you don't have permissions"})
            users.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class TrackList(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    name = 'track-list'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['kierownik-przewozu-smieci'],
        'POST': ['kierownik-przewozu-smieci'],
    }


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    name = 'track-detail'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['kierownik-przewozu-smieci'],
        'PUT': ['kierownik-przewozu-smieci'],
        'DELETE': [],
    }


class BinTrackList(generics.ListCreateAPIView):
    queryset = BinTrack.objects.all()
    serializer_class = BinTrackSerializer
    name = 'bin-track-list'
    filter_fields = ['track']
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['kierownik-przewozu-smieci'],
        'POST': ['kierownik-przewozu-smieci'],
    }


class BinTrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BinTrack.objects.all()
    serializer_class = BinTrackSerializer
    name = 'bin-track-detail'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['kierownik-przewozu-smieci'],
        'PUT': ['kierownik-przewozu-smieci'],
        'DELETE': [],
    }


class InvoicesList(generics.ListCreateAPIView):
    queryset = Invoices.objects.all()
    serializer_class = InvoicesSerializer
    name = 'invoices-list'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['ksiegowa'],
        'POST': ['ksiegowa'],
    }


class InvoicesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoices.objects.all()
    serializer_class = InvoicesSerializer
    name = 'invoices-detail'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['ksiegowa'],
        'PUT': ['ksiegowa'],
        'DELETE': [],
    }


class InvoicesNamesList(generics.ListCreateAPIView):
    queryset = InvoicesNames.objects.all()
    serializer_class = InvoicesNamesSerializer
    name = 'invoices-names-list'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['ksiegowa'],
        'POST': ['ksiegowa'],
    }


class InvoicesNamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoicesNames.objects.all()
    serializer_class = InvoicesNamesSerializer
    name = 'invoices-names-detail'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['ksiegowa'],
        'PUT': ['ksiegowa'],
        'DELETE': [],
    }


class ScheduleList(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    name = 'schedule-list'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['kierowca-smieciarki', 'pracownik-wysypiska', 'pracownicy-przewozacy-smieci', 'kierownik-wysypiska',
                'kierownik-przewozu-smieci'],
        'POST': ['kierownik-wysypiska', 'kierownik-przewozu-smieci'],
    }


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    name = 'schedule-detail'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['kierownik-wysypiska', 'kierownik-przewozu-smieci'],
        'PUT': ['kierownik-wysypiska', 'kierownik-przewozu-smieci'],
        'DELETE': ['kierownik-wysypiska', 'kierownik-przewozu-smieci'],
    }


class KeysList(generics.ListCreateAPIView):
    queryset = Keys.objects.all()
    serializer_class = KeysSerializer
    name = 'keys-list'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['kierowca-smieciarki', 'pracownik-wysypiska', 'pracownicy-przewozacy-smieci', 'kierownik-wysypiska',
                'kierownik-przewozu-smieci'],
        'POST': ['kierownik-wysypiska', 'kierownik-przewozu-smieci'],
    }


class KeysDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Keys.objects.all()
    serializer_class = KeysSerializer
    name = 'keys-detail'
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {
        'GET': ['kierownik-wysypiska', 'kierownik-przewozu-smieci'],
        'PUT': ['kierownik-wysypiska', 'kierownik-przewozu-smieci'],
        'DELETE': ['kierownik-wysypiska', 'kierownik-przewozu-smieci'],
    }


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'cars': reverse(CarList.name, request=request),
                         'users': reverse(UserList.name, request=request),
                         'trash-bins': reverse(TrashBinList.name, request=request),
                         'bin-tracks': reverse(BinTrackList.name, request=request),
                         'garbage-dumps': reverse(GarbageDumpList.name, request=request),
                         'tracks': reverse(TrackList.name, request=request),
                         'invoices': reverse(InvoicesList.name, request=request),
                         'invoices-names': reverse(InvoicesNamesList.name, request=request),
                         'schedules': reverse(ScheduleList.name, request=request),
                         'keys': reverse(KeysList.name, request=request),
                         })
