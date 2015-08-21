# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paradigm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=64)),
                ('is_visible', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='programminglanguage',
            name='is_visible',
            field=models.BooleanField(default=False),
        ),
    ]
