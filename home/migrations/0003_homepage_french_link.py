# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0002_languageredirectionpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='french_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]
