from multiprocessing import get_context
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from blog.models import BlogIndexPage, BlogPage


class Noticia(models.Model):
    pass

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        indice_noticias = BlogIndexPage.objects.filter(title="Noticias Peliculas")
        if indice_noticias:
            indice_noticias = indice_noticias[0]
            noticias = BlogPage.objects.descendant_of(indice_noticias).order_by("-date")[:5]
            context['noticias'] = noticias
        return context