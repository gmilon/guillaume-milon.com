# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 16:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20171013_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(blank=True, max_length=250)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_lines', to='home.HomePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(blank=True, max_length=300)),
                ('subtitle', models.CharField(blank=True, max_length=300)),
                ('orientation', models.CharField(choices=[('timeline-unverted', 'right'), ('timeline-inverted', 'left')], max_length=100)),
                ('text', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('logo', models.CharField(blank=True, choices=[('icon-linkedin2', 'linkedn'), ('icon-facebook2', 'Facebook'), ('icon-twitter2', 'Twitter'), ('icon-graduation-cap', 'Graduation'), ('icon-suitcase', 'Suitecase')], max_length=250)),
                ('related_time_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.TimeLine')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='logo_class',
            field=models.CharField(blank=True, choices=[('icon-linkedin2', 'linkedn'), ('icon-facebook2', 'Facebook'), ('icon-twitter2', 'Twitter'), ('icon-graduation-cap', 'Graduation'), ('icon-suitcase', 'Suitecase')], max_length=250),
        ),
    ]
