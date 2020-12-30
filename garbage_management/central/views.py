from django.http import Http404
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .permissions import HasGroupPermission
from rest_framework.response import Response
from rest_framework import status
from .models import Cars, TrashBin, GarbageDump, Track
from .serializers import CarsSerializer, TrashBinSerializer, GarbageDumpSerializer, UserSerializer, UserModifySerializer, TrackSerializer
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
    """
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['szef', 'kierownik-glowny', 'kierownik-przewozu-smieci', 'kierownik-wysypiska'],
        'POST': ['szef', 'kierownik-glowny', 'kierownik-przewozu-smieci', 'kierownik-wysypiska'],
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


    def post(self, request, format=None):
        current_user = User.objects.all().filter(username=request.user).first()
        serializer = UserSerializer(current_user)
        if 'szef' in serializer.data['groups']:
            available_groups = ['kierowca-smieciarki', 'kierownik-glowny', 'kierownik-przewozu-smieci',
                                'kierownik-wysypiska', 'ksiegowosc', 'pracownicy-przewozacy-smieci',
                                'pracownik-wysypiska', 'szef']
            serializer2 = UserModifySerializer(data=request.data)
            if serializer2.is_valid():
                print(serializer2.validated_data)
                if serializer2.validated_data['groups'] not in available_groups:
                    return Response({"error": "That group is out of your permissions"}, status=status.HTTP_400_BAD_REQUEST)
                serializer2.save()
                return Response(serializer2.data)
            return Response(serializer2.errors)

        if 'kierownik-glowny' in serializer.data['groups']:
            available_groups = ['kierowca-smieciarki', 'kierownik-glowny', 'kierownik-przewozu-smieci',
                                'kierownik-wysypiska', 'ksiegowosc', 'pracownicy-przewozacy-smieci',
                                'pracownik-wysypiska']
            serializer2 = UserModifySerializer(data=request.data)
            if serializer2.is_valid():
                print(serializer2.validated_data)
                if serializer2.validated_data['groups'] not in available_groups:
                    return Response({"error": "That group is out of your permissions"}, status=status.HTTP_400_BAD_REQUEST)
                serializer2.save()
                return Response(serializer2.data)
            return Response(serializer2.errors)

        if 'kierownik-przewozu-smieci' in serializer.data['groups']:
            available_groups = ['kierowca-smieciarki', 'pracownicy-przewozacy-smieci']
            serializer2 = UserModifySerializer(data=request.data)
            if serializer2.is_valid():
                print(serializer2.validated_data)
                if serializer2.validated_data['groups'] not in available_groups:
                    return Response({"error": "That group is out of your permissions"}, status=status.HTTP_400_BAD_REQUEST)
                serializer2.save()
                return Response(serializer2.data)
            return Response(serializer2.errors)

        if 'kierownik-wysypiska' in serializer.data['groups']:
            available_groups = ['pracownik-wysypiska']
            serializer2 = UserModifySerializer(data=request.data)
            if serializer2.is_valid():
                print(serializer2.validated_data)
                if serializer2.validated_data['groups'] not in available_groups:
                    return Response({"error": "That group is out of your permissions"}, status=status.HTTP_400_BAD_REQUEST)
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
        'GET': ['kps', 'members'],
        'POST': ['kps', 'someMadeUpGroup'],
    }

    def get(self, request, format=None):
        # TODO
        # get a list of tracks
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # TODO
        # create a new track
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class TrackDetailsView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kps', 'members'],
        'PUT': ['__all__'],
        'DELETE': ['kps'],
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
        'GET': ['kps', 'members'],
        'POST': ['kps', 'someMadeUpGroup'],
    }

    def get(self, request, format=None):
        # TODO
        # get int track_id
        # get list of stops on the track
        pass

    def post(self, request, format=None):
        # TODO
        # add new stop to the track
        pass


class BinTrackDetailsView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kps', 'members'],
        'POST': ['kps', 'someMadeUpGroup'],
        'PUT': ['__all__'],
        'DELETE': ['kps'],
    }

    def get(self, request, pk, format=None):
        # TODO
        # get stop id
        pass

    def put(self, request, pk, format=None):
        # TODO
        # update the stop
        pass

    def delete(self, request, pk, format=None):
        # TODO
        # delete the stop
        pass


class InvoicesView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kps', 'members'],
        'POST': ['kps', 'someMadeUpGroup'],
        'PUT': ['__all__'],
        'DELETE': ['kps'],
    }

    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass


class InvoicesDetailsView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kps', 'members'],
        'POST': ['kps', 'someMadeUpGroup'],
        'PUT': ['__all__'],
        'DELETE': ['kps'],
    }

    def get(self, request, pk, format=None):
        pass

    def put(self, request, pk, format=None):
        pass

    def delete(self, request, pk, format=None):
        pass


class ScheduleView(APIView):
    permission_classes = [IsAuthenticated, HasGroupPermission]  # Ustawianie klas zezwolen
    required_groups = {
        'GET': ['kps', 'members'],
        'POST': ['kps', 'someMadeUpGroup'],
        'PUT': ['__all__'],
        'DELETE': ['kps'],
    }

    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass


class ScheduleDetailsView(APIView):
    def get(self, request, pk, format=None):
        pass

    def put(self, request, pk, format=None):
        pass

    def delete(self, request, pk, format=None):
        pass
