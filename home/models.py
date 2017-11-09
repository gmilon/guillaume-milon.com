from __future__ import absolute_import, unicode_literals

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtailgmaps.edit_handlers import MapFieldPanel
from wagtail.wagtailcore.models import Page

from django.utils import translation
from django.http import HttpResponseRedirect

from home.views import TranslatablePageMixin

LINKDN = 'icon-linkedin2'
FB = 'icon-facebook2'
TW = 'icon-twitter2'
SUIT_CASE = 'icon-suitcase'
GRAD = 'icon-graduation-cap'
PAINTBRUSH = 'icon-paintbrush'
BRIEFCASE = 'icon-briefcase'
SEARCH = 'icon-search'
BARGRAPH = 'icon-bargraph'
GENIUS = 'icon-genius'
CHAT = 'icon-chat'


LOGOS_CLASSES = [
    (LINKDN, 'linkedn'),
    (FB, 'Facebook'),
    (TW, 'Twitter'),
    (GRAD, 'Graduation'),
    (SUIT_CASE, 'Suitecase'),
    (PAINTBRUSH, 'Paint brush'),
    (BRIEFCASE, 'briefcase'),
    (SEARCH, 'search'),
    (BARGRAPH, 'bargraph'),
    (CHAT, 'chat')
]


class LanguageRedirectionPage(Page):

    def serve(self, request):
        # This will only return a language that is in the LANGUAGES Django setting
        language = translation.get_language_from_request(request)

        return HttpResponseRedirect(self.url + language + '/')


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class HomePage(Page, TranslatablePageMixin):

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

    # work XP and studies
    wx_title = models.CharField(null=True, blank=True, max_length=300)
    studies_title = models.CharField(null=True, blank=True, max_length=300)

    # services
    services_title = models.CharField(blank=True, max_length=250)

    # skills
    skill_title = models.CharField(blank=True, max_length=250)

    # Position
    position = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(TranslatablePageMixin.panels, 'Language links'),
        MultiFieldPanel(
            [
                InlinePanel('socials', label="Socials Media"),
                ImageChooserPanel('header_img'),
                ImageChooserPanel('header_bg'),
                FieldPanel('header_title'),
                FieldPanel('header_subtitle'),
            ],
            heading="Header section",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('about_title'),
                FieldPanel('about_text', classname="full"),
            ],
            heading="About section",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('wx_title'),
                InlinePanel('time_line_work', label="Work Experiences"),
                FieldPanel('studies_title'),
                InlinePanel('time_line_study', label="Studies"),
            ],
            heading="Experience section",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('services_title'),
                InlinePanel('services', label="Services"),
            ],
            heading="Experience section",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('skill_title'),
                InlinePanel('skills', label="Skills"),
            ],
            heading="Experience section",
            classname="collapsible collapsed"
        ),
        MapFieldPanel('position', latlng=True)
    ]


class SocialMedia(Orderable):
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


class TimeLineWorkXP(Orderable):
    related_time_work = ParentalKey(HomePage, related_name='time_line_work')

    title = models.CharField(blank=True, max_length=300)
    subtitle = models.CharField(blank=True, max_length=300)
    orientation = models.CharField(
        blank=False,
        max_length=100,
        choices=[
            ('timeline-unverted', 'right'),
            ('timeline-inverted', 'left'),
        ]
    )
    text = RichTextField(blank=True)
    logo = models.CharField(blank=True, choices=LOGOS_CLASSES, max_length=250)


class TimeLineStudies(Orderable):
    related_time_studies = ParentalKey(HomePage, related_name='time_line_study')

    title = models.CharField(blank=True, max_length=300)
    subtitle = models.CharField(blank=True, max_length=300)
    orientation = models.CharField(
        blank=False,
        max_length=100,
        choices=[
            ('timeline-unverted', 'right'),
            ('timeline-inverted', 'left'),
        ]
    )
    text = RichTextField(blank=True)
    logo = models.CharField(blank=True, choices=LOGOS_CLASSES, max_length=250)


class Services(Orderable):
    parent = ParentalKey(HomePage, related_name='services')
    title = models.CharField(max_length=250)
    logo = models.CharField(blank=True, choices=LOGOS_CLASSES, max_length=250)
    text = models.TextField(blank=True)


class Skill(Orderable):
    parent = ParentalKey(HomePage, related_name='skills')
    title = models.CharField(max_length=250)
    value = IntegerRangeField(max_value=100, min_value=0)
    color = models.CharField(max_length=250)
    graph_type = models.CharField(
        max_length=250,
        default='bar',
        choices=[
            ('bar', 'bar'),
            ('circle', 'circle'),
        ]
    )
