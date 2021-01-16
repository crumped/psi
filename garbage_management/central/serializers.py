from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group


class BinTrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = BinTrack
        fields = '__all__'
        read_only_fields = ('id_bin_track',)


class CarTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarType
        fields = '__all__'
        read_only_fields = ('id_car_type',)


class CarsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cars
        fields = '__all__'
        read_only_fields = ('id_cars',)


class GarbageDumpSerializer(serializers.ModelSerializer):

    class Meta:
        model = GarbageDump
        fields = '__all__'
        read_only_fields = ('id_garbage_dump',)


class KeysSerializer(serializers.ModelSerializer):
    driver = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field="username")
    supervisor = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field="username")
    car = serializers.SlugRelatedField(queryset=Cars.objects.all(), slug_field="number_plate")

    class Meta:
        model = Keys
        fields = '__all__'
        read_only_fields = ('id_keys',)


class InvoicesNamesSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoicesNames
        fields = '__all__'
        read_only_fields = ('id_invoices_names',)


class InvoicesSerializer(serializers.ModelSerializer):
    invoices = InvoicesNamesSerializer(many=True, read_only=True)

    class Meta:
        model = Invoices
        fields = '__all__'
        read_only_fields = ('id_invoices',)

    depth = 1


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = '__all__'
        read_only_fields = ('id_schedule',)


class TrackSerializer(serializers.ModelSerializer):
    stops = BinTrackSerializer(many=True, read_only=True)
    car = serializers.SlugRelatedField(queryset=Cars.objects.all(), slug_field="number_plate")
    garbage_dump = serializers.SlugRelatedField(queryset=GarbageDump.objects.all(), slug_field="address")

    class Meta:
        model = Track
        fields = '__all__'
        read_only_fields = ('id_track',)


class TrashBinSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrashBin
        fields = '__all__'
        read_only_fields = ('id_trash_bin',)


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                  'is_active', 'is_staff', 'is_superuser', 'date_joined', 'groups',)
        read_only_fields = ('username', 'auth_token', 'date_joined', 'groups', 'is_staff', 'is_superuser',)


class UserModifySerializer(serializers.ModelSerializer):
    groups = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'groups', 'password')
        read_only_fields = ('auth_token', 'date_joined')
        extra_kwargs = {'password': {'write_only': True}, 'groups': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['is_active'] = 1
        group = validated_data.pop('groups')
        user = User(**validated_data)
        user.set_password(password)
        g = Group.objects.get(name=group)
        user.save()
        user.groups.add(g)
        return user
