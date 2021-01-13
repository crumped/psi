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
from .pagination import PaginationHandlerMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.reverse import reverse


def index(request):
    return render(request, 'html/main.html')


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


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


class TrashBinDetailsView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kierownik-przewozu-smieci'],
        'PUT': ['kierownik-przewozu-smieci'],
        'DELETE': ['kierownik-przewozu-smieci'],
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


class TrashBinsView(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kierownik-przewozu-smieci'],
        'POST': ['kierownik-przewozu-smieci'],
    }

    def get(self, request, format=None):
        trash_bins = TrashBin.objects.all().order_by('id_trash_bin')
        page = self.paginate_queryset(trash_bins)
        if page is not None:
            serializer = self.get_paginated_response(TrashBinSerializer(page, many=True).data)
        else:
            serializer = TrashBinSerializer(trash_bins, many=True)
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
        'GET': ['kierownik-przewozu-smieci', 'kierownik-wysypiska'],
        'PUT': ['kierownik-wysypiska'],
        'DELETE': ['kierownik-wysypiska'],
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
        'GET': ['kierownik-przewozu-smieci', 'kierownik-wysypiska'],
        'POST': ['kierownik-wysypiska'],
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


class TrackView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kierownik-przewozu-smieci'],
        'POST': ['kierownik-przewozu-smieci'],
    }

    def get(self, request, format=None):
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class TrackDetailsView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kierownik-przewozu-smieci'],
        'PUT': ['kierownik-przewozu-smieci'],
        'DELETE': [],
    }

    def get(self, request, pk, format=None):
        track = Track.objects.get(pk=pk)
        serializer = TrackSerializer(track)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        track = Track.objects.get(pk=pk)
        serializer = TrackSerializer(track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        track = Track.objects.get(pk=pk)
        track.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BinTrackView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kierownik-przewozu-smieci'],
        'POST': ['kierownik-przewozu-smieci'],
    }

    def get(self, request, format=None):
        track_id = request.query_params.get('track-id', None)
        if track_id is not None:
            print(track_id)
            tracks = BinTrack.objects.all().filter(track=track_id)
            serializer = BinTrackSerializer(tracks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"missing track-id parameter"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = BinTrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class BinTrackDetailsView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kierownik-przewozu-smieci'],
        'PUT': ['kierownik-przewozu-smieci'],
        'DELETE': [],
    }

    def get(self, request, pk, format=None):
        bin_track = BinTrack.objects.get(pk=pk)
        serializer = BinTrackSerializer(bin_track)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        bin_track = BinTrack.objects.get(pk=pk)
        serializer = BinTrackSerializer(bin_track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bin_track = BinTrack.objects.get(pk=pk)
        bin_track.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InvoicesView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['ksiegowa'],
        'POST': ['ksiegowa'],
    }

    def get(self, request, format=None):
        invoices = Invoices.objects.all()
        serializer = InvoicesSerializer(invoices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = InvoicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class InvoicesDetailsView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['ksiegowa'],
        'PUT': ['ksiegowa'],
        'DELETE': [],
    }

    def get(self, request, pk, format=None):
        invoices = Invoices.objects.get(pk=pk)
        serializer = InvoicesSerializer(invoices)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        invoices = Invoices.objects.get(pk=pk)
        serializer = InvoicesSerializer(invoices, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        invoices = Invoices.objects.get(pk=pk)
        invoices.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InvoicesNamesView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['ksiegowa'],
        'POST': ['ksiegowa'],
    }

    def get(self, request, format=None):
        invoices = InvoicesNames.objects.all()
        serializer = InvoicesNamesSerializer(invoices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = InvoicesNamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class InvoicesNamesDetailsView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['ksiegowa'],
        'PUT': ['ksiegowa'],
    }

    def get(self, request, pk, format=None):
        invoices = InvoicesNames.objects.get(pk=pk)
        serializer = InvoicesNamesSerializer(invoices)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        invoices = InvoicesNames.objects.get(pk=pk)
        serializer = InvoicesNamesSerializer(invoices, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kierowca-smieciarki', 'pracownik-wysypiska', 'pracownicy-przewozacy-smieci', 'kierownik-wysypiska',
                'kierownik-przewozu-smieci'],
        'POST': ['kierownik-wysypiska', 'kierownik-przewozu-smieci'],
    }

    def get(self, request, format=None):
        this_month = datetime.datetime.now().month
        schedule = Schedule.objects.all().filter(day__month=this_month)
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class ScheduleDetailsView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kierownik-wysypiska', 'kierownik-przewozu-smieci'],
        'PUT': ['kierownik-wysypiska', 'kierownik-przewozu-smieci'],
        'DELETE': ['kierownik-wysypiska', 'kierownik-przewozu-smieci'],
    }

    def get(self, request, pk, format=None):
        schedule = Schedule.objects.get(pk=pk)
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        schedule = Schedule.objects.get(pk=pk)
        serializer = ScheduleSerializer(schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        schedule = Schedule.objects.get(pk=pk)
        schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class KeysView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kierownik-przewozu-smieci'],
        'POST': ['kierownik-przewozu-smieci'],
    }

    def get(self, request, format=None):
        keys = Keys.objects.all()
        serializer = KeysSerializer(keys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer =KeysSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class KeysDetailsView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kierownik-przewozu-smieci'],
        'PUT': ['kierownik-przewozu-smieci'],
        'DELETE': ['kierownik-przewozu-smieci'],
    }

    def get(self, request, pk, format=None):
        keys = Keys.objects.get(pk=pk)
        serializer = KeysSerializer(keys)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        keys = Keys.objects.get(pk=pk)
        serializer = KeysSerializer(keys, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        keys = Keys.objects.get(pk=pk)
        keys.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'cars': reverse(CarList.name, request=request),
                         'users': reverse(UserList.name, request=request),
                         })
