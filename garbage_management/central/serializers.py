from rest_framework import serializers
from .models import *


class BinTrack(serializers.ModelSerializer):

    class Meta:
        model = BinTrack
        fields = '__all__'
        read_only_fields = ('id_bin_track',)


class CarGps(serializers.ModelSerializer):

    class Meta:
        model = CarGps
        fields = '__all__'
        read_only_fields = ('id_car_gps',)


class CarType(serializers.ModelSerializer):

    class Meta:
        model = CarType
        fields = '__all__'
        read_only_fields = ('id_car_type',)


class Cars(serializers.ModelSerializer):

    class Meta:
        model = Cars
        fields = '__all__'
        read_only_fields = ('id_cars',)


class GarbageDump(serializers.ModelSerializer):

    class Meta:
        model = GarbageDump
        fields = '__all__'
        read_only_fields = ('id_garbage_dump',)


class Invoices(serializers.ModelSerializer):

    class Meta:
        model = Invoices
        fields = '__all__'
        read_only_fields = ('id_invoices',)


class InvoicesNames(serializers.ModelSerializer):

    class Meta:
        model = InvoicesNames
        fields = '__all__'
        read_only_fields = ('id_invoices_names',)


class ReportProblem(serializers.ModelSerializer):

    class Meta:
        model = ReportProblem
        fields = '__all__'
        read_only_fields = ('id_report_problem',)


class Track(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = '__all__'
        read_only_fields = ('id_track',)


class TrashBin(serializers.ModelSerializer):

    class Meta:
        model = TrashBin
        fields = '__all__'
        read_only_fields = ('id_trash_bin',)
