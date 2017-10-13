from __future__ import absolute_import, unicode_literals

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):

    header_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    header_bg = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    header_title = models.CharField(null=True, blank=True, max_length=200)
    header_subtitle = models.CharField(null=True, blank=True, max_length=200)

    # About Me Section
    about_title = models.CharField(null=True, blank=True, max_length=300)
    about_text = RichTextField(blank=True)

    # My Resume
    mr_title = models.CharField(null=True, blank=True, max_length=300)
    mr_text = RichTextField(blank=True)


    content_panels = Page.content_panels + [
        ImageChooserPanel('header_img'),
        ImageChooserPanel('header_bg'),
        FieldPanel('header_title'),
        FieldPanel('header_subtitle'),
        FieldPanel('about_title'),
        FieldPanel('about_text', classname="full"),
        InlinePanel('socials', label="Socials Media"),
    ]


class SocialMedia(Orderable):
    LINKDN = 'icon-linkedin2'
    FB = 'icon-facebook2'
    TW = 'icon-twitter2'
    LOGOS_CLASSES = [
        (LINKDN, 'linkedn'),
        (FB, 'Facebook'),
        (TW, 'Twitter'),
    ]
    page = ParentalKey(HomePage, related_name='socials')
    title = models.CharField(blank=True, max_length=250)
    logo_class = models.CharField(blank=True, choices=LOGOS_CLASSES, max_length=250)
    logo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    url = models.URLField(blank=True, null=True)

