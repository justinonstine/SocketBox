# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('size', models.CharField(max_length=30)),
                ('unitType', models.CharField(default=b'IM', max_length=2, choices=[(b'ME', b'Metric'), (b'IM', b'Imperial')])),
                ('description', models.CharField(max_length=500)),
                ('lastLoaned', models.DateField()),
                ('dueDate', models.DateField()),
                ('accessory', models.ManyToManyField(to='socketbox.Tool')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('address', models.ForeignKey(related_name='home_address', to='socketbox.Location')),
                ('communities', models.ManyToManyField(to='socketbox.Community')),
                ('locations', models.ManyToManyField(to='socketbox.Location')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tool',
            name='caretaker',
            field=models.ForeignKey(related_name='caretaker', to='socketbox.UserProfile'),
        ),
        migrations.AddField(
            model_name='tool',
            name='category',
            field=models.ManyToManyField(to='socketbox.Category'),
        ),
        migrations.AddField(
            model_name='tool',
            name='currentLocation',
            field=models.ForeignKey(related_name='current_location', to='socketbox.Location'),
        ),
        migrations.AddField(
            model_name='tool',
            name='owners',
            field=models.ManyToManyField(to='socketbox.UserProfile'),
        ),
        migrations.AddField(
            model_name='tool',
            name='permanentLocation',
            field=models.ForeignKey(related_name='permanent_location', to='socketbox.Location'),
        ),
        migrations.AddField(
            model_name='tool',
            name='set',
            field=models.ForeignKey(to='socketbox.Set'),
        ),
    ]
