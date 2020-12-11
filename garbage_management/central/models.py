# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BinTrack(models.Model):
    id_bin_track = models.IntegerField(primary_key=True)
    bin = models.ForeignKey('TrashBin', models.DO_NOTHING, blank=True, null=True)
    track = models.ForeignKey('Track', models.DO_NOTHING, blank=True, null=True)
    stop_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bin_track'


class CarGps(models.Model):
    id_car_gps = models.AutoField(primary_key=True)
    position = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_create = models.DateTimeField()
    car = models.ForeignKey('Cars', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_gps'


class CarType(models.Model):
    id_car_type = models.AutoField(primary_key=True)
    type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_type'


class Cars(models.Model):
    id_cars = models.AutoField(primary_key=True)
    number_plate = models.CharField(max_length=45, blank=True, null=True)
    car_type = models.ForeignKey(CarType, models.DO_NOTHING, db_column='car_type', blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    date_oil = models.DateField(blank=True, null=True)
    mileage_oil = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars'


class GarbageDump(models.Model):
    id_garbage_dump = models.AutoField(primary_key=True)
    address_gps = models.TextField(blank=True, null=True)  # This field type is a guess.
    address = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'garbage_dump'


class Invoices(models.Model):
    id_invoices = models.IntegerField(primary_key=True)
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
    id_invoices_names = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    adress = models.CharField(max_length=100, blank=True, null=True)
    nip = models.IntegerField(blank=True, null=True)
    invoices = models.ForeignKey(Invoices, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices_names'


class ReportProblem(models.Model):
    id_report_problem = models.AutoField(primary_key=True)
    type_of_report = models.CharField(max_length=45, blank=True, null=True)
    date_reported = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    car = models.ForeignKey(Cars, models.DO_NOTHING, blank=True, null=True)
    bin = models.ForeignKey('TrashBin', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_problem'


class Track(models.Model):
    id_track = models.AutoField(primary_key=True)
    arrival_date = models.DateTimeField(blank=True, null=True)
    is_done = models.IntegerField(blank=True, null=True)
    car = models.ForeignKey(Cars, models.DO_NOTHING, blank=True, null=True)
    driver = models.IntegerField(blank=True, null=True)
    manager = models.IntegerField(blank=True, null=True)
    date_of_loan_keys = models.DateTimeField(blank=True, null=True)
    date_return_keys = models.DateTimeField(blank=True, null=True)
    garbage_dump = models.ForeignKey(GarbageDump, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'track'


class TrashBin(models.Model):
    id_trash_bin = models.AutoField(primary_key=True)
    bin_capacity = models.CharField(max_length=45, blank=True, null=True)
    bin_type = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    bin_size = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trash_bin'
