# Generated by Django 4.0.5 on 2022-06-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=50)),
                ('aname', models.CharField(max_length=25)),
                ('price', models.BigIntegerField()),
            ],
        ),
    ]