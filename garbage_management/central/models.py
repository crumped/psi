# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


def get_first_name(self):
    return self.username


User.add_to_class("__str__", get_first_name)


class BinTrack(models.Model):
    id_bin_track = models.AutoField(primary_key=True)
    bin = models.ForeignKey('TrashBin', on_delete=models.SET_NULL, blank=True, null=True)
    track = models.ForeignKey('Track', on_delete=models.CASCADE, related_name='stops', blank=True, null=False)
    stop_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bin_track'
        ordering = ['stop_number']


class CarType(models.Model):
    id_car_type = models.AutoField(primary_key=True)
    type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_type'


class Cars(models.Model):
    id_cars = models.AutoField(primary_key=True)
    number_plate = models.CharField(max_length=45, blank=False, null=False)
    car_type = models.ForeignKey(CarType, on_delete=models.SET_NULL, db_column='car_type', blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    date_oil = models.DateField(blank=True, null=True)
    mileage_oil = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars'

    def __str__(self):
        return self.number_plate


class GarbageDump(models.Model):
    id_garbage_dump = models.AutoField(primary_key=True)
    address_gps = models.TextField(blank=True, null=True)  # This field type is a guess.
    address = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'garbage_dump'

    def __str__(self):
        return self.address


class Invoices(models.Model):
    id_invoices = models.AutoField(primary_key=True)
    number = models.IntegerField(blank=True, null=True)
    date_of_invoice = models.DateTimeField(blank=True, null=True)
    date_of_service = models.DateTimeField(blank=True, null=True)
    name_of_service = models.CharField(max_length=100, blank=True, null=True)
    number_of_items = models.IntegerField(blank=True, null=True)
    price_netto = models.IntegerField(blank=True, null=True)
    full_price_netto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices'


class InvoicesNames(models.Model):
    id_invoices_names = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nip = models.IntegerField(blank=True, null=True)
    invoices = models.ForeignKey(Invoices, on_delete=models.SET_NULL, related_name='invoices', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices_names'


class Keys(models.Model):
    id_keys = models.AutoField(primary_key=True)
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, db_column='driver', related_name="driver", blank=True,
                               null=True)
    supervisor = models.ForeignKey(User, on_delete=models.SET_NULL, db_column='supervisor', related_name="supervisor",
                                   blank=True, null=True)
    car = models.ForeignKey(Cars, on_delete=models.SET_NULL, db_column='car_id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keys'
        ordering = ['id_keys']


class Schedule(models.Model):
    id_schedule = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    day = models.DateField(blank=True, null=True)
    work_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'


class Track(models.Model):
    id_track = models.AutoField(primary_key=True)
    arrival_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    is_done = models.IntegerField(blank=True, null=True)
    car = models.ForeignKey(Cars, on_delete=models.SET_NULL, blank=True, null=True)
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, db_column='driver', blank=True, null=True)
    manager = models.IntegerField(blank=True, null=True)
    garbage_dump = models.ForeignKey(GarbageDump, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'track'
        ordering = ['id_track']


class TrashBin(models.Model):
    id_trash_bin = models.AutoField(primary_key=True)
    bin_capacity = models.CharField(max_length=45, blank=True, null=True)
    bin_type = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    bin_size = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trash_bin'

    def __str__(self):
        return self.address
