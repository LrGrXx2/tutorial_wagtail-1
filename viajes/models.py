from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your models here.
class Viaje(models.Model):
    nombre = models.CharField('nombre', max_length=250)
    #slug = models.SlugField(blank=True, max_length=250)
    link = models.URLField()
    coordenadas = models.CharField("coordenadas", max_length = 100, blank = True)
    imagen = models.URLField(max_length=250)

    panels = [
        FieldPanel('nombre'),
        #FieldPanel('slug'),
        FieldPanel('link'),
        FieldPanel('coordenadas'),
        FieldPanel('imagen')

    ]
    def __str__(self):
        return f'{self.nombre}'
    
    class Meta:
        verbose_name = 'Viaje'
        verbose_name_plural = 'Viajes'

class ViajesPage(Page):
    texto = RichTextField(blank=True)
    coordenadas = RichTextField(blank=True, max_length = 100)

    content_panels = Page.content_panels + [
        FieldPanel('texto', classname="full"),
        FieldPanel('coordenadas', classname="full")
    ]

    def paginate(self, request, viajes, *args):
        page = request.GET.get('page')
        
        paginator = Paginator(viajes, 10)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages
