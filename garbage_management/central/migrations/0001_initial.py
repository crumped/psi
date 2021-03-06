# Generated by Django 3.1.3 on 2021-01-04 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id_cars', models.AutoField(primary_key=True, serialize=False)),
                ('number_plate', models.CharField(max_length=45)),
                ('mileage', models.IntegerField(blank=True, null=True)),
                ('date_oil', models.DateField(blank=True, null=True)),
                ('mileage_oil', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cars',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id_car_type', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'car_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GarbageDump',
            fields=[
                ('id_garbage_dump', models.AutoField(primary_key=True, serialize=False)),
                ('address_gps', models.TextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('category', models.CharField(blank=True, max_length=7, null=True)),
            ],
            options={
                'db_table': 'garbage_dump',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id_invoices', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('date_of_invoice', models.DateTimeField(blank=True, null=True)),
                ('date_of_service', models.DateTimeField(blank=True, null=True)),
                ('name_of_service', models.CharField(blank=True, max_length=100, null=True)),
                ('number_of_items', models.IntegerField(blank=True, null=True)),
                ('price_netto', models.IntegerField(blank=True, null=True)),
                ('full_price_netto', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'invoices',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TrashBin',
            fields=[
                ('id_trash_bin', models.AutoField(primary_key=True, serialize=False)),
                ('bin_capacity', models.CharField(blank=True, max_length=45, null=True)),
                ('bin_type', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('bin_size', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'trash_bin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id_track', models.AutoField(primary_key=True, serialize=False)),
                ('arrival_date', models.DateTimeField(blank=True, null=True)),
                ('is_done', models.IntegerField(blank=True, null=True)),
                ('driver', models.IntegerField(blank=True, null=True)),
                ('manager', models.IntegerField(blank=True, null=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='central.cars')),
                ('garbage_dump', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='central.garbagedump')),
            ],
            options={
                'db_table': 'track',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id_schedule', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.DateField(blank=True, null=True)),
                ('work_type', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'schedule',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Keys',
            fields=[
                ('id_keys', models.AutoField(primary_key=True, serialize=False)),
                ('car', models.ForeignKey(blank=True, db_column='car_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='central.cars')),
                ('driver', models.ForeignKey(blank=True, db_column='driver', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='driver', to=settings.AUTH_USER_MODEL)),
                ('supervisor', models.ForeignKey(blank=True, db_column='supervisor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='supervisor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'keys',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InvoicesNames',
            fields=[
                ('id_invoices_names', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('nip', models.IntegerField(blank=True, null=True)),
                ('invoices', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoices', to='central.invoices')),
            ],
            options={
                'db_table': 'invoices_names',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='cars',
            name='car_type',
            field=models.ForeignKey(blank=True, db_column='car_type', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='central.cartype'),
        ),
        migrations.CreateModel(
            name='BinTrack',
            fields=[
                ('id_bin_track', models.AutoField(primary_key=True, serialize=False)),
                ('stop_number', models.IntegerField(blank=True, null=True)),
                ('bin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='central.trashbin')),
                ('track', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stops', to='central.track')),
            ],
            options={
                'db_table': 'bin_track',
                'managed': True,
            },
        ),
    ]
