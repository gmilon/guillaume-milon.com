from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):

    header_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    header_title = models.CharField(null=True, blank=True, max_length=200)

    header_subtitle = models.CharField(null=True, blank=True, max_length=200)

    content_panels = Page.content_panels + [
        ImageChooserPanel('header_img'),
        FieldPanel('header_title'),
        FieldPanel('header_subtitle'),
    ]
