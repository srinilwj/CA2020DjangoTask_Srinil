# Generated by Django 2.2 on 2020-07-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('Name', models.CharField(max_length=100)),
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Contact', models.IntegerField()),
                ('Address', models.CharField(max_length=300)),
            ],
        ),
    ]
