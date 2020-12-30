# Generated by Django 3.1.3 on 2020-12-30 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keys',
            fields=[
                ('id_keys', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'keys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id_schedule', models.IntegerField(primary_key=True, serialize=False)),
                ('day', models.DateField(blank=True, null=True)),
                ('work_type', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'schedule',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='CarGps',
        ),
        migrations.DeleteModel(
            name='ReportProblem',
        ),
    ]