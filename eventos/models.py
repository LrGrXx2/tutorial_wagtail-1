from django.db import models

from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.snippets.models import register_snippet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify


# Create your models here.

## Page que mostrará el index de las películas
## Hereda solo de Home y no descendientes

# Modelo de Evento
class Evento(models.Model):
    nombre = models.CharField('nombre', max_length=250)
    #slug = models.SlugField(blank=True, max_length=250)
    descripcion = models.CharField('descripcion', max_length=500)
    imagen = models.URLField(max_length=250)
    fecha_inicio = models.DateField()
    categoria = models.CharField('categoria', max_length=250)
    autor = models.CharField('autor', max_length=250)

    panels = [
        FieldPanel('nombre'),
        #FieldPanel('slug'),
        FieldPanel('descripcion'),
        FieldPanel('imagen'),
        FieldPanel('fecha_inicio'),
        FieldPanel('categoria'),
        FieldPanel('autor')

    ]
    def __str__(self):
        return f'{self.nombre} ({self.fecha_inicio})'
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        

class EventosIndexPage(Page):
    introduccionEventos = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccionEventos', classname="full")
    ]
    subpage_types = []

    def paginate(self, request, eventos, *args):
        page = request.GET.get('page')
        
        paginator = Paginator(eventos, 3)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        fecha_inicio = request.GET.get('fecha_inicio')
        qs = ''
        if fecha_inicio:
            eventos = Evento.objects.filter(year__gte=1990, 
                year__lt=2000).order_by('fecha_inicio')
            qs = f'fecha_inicio={fecha_inicio}'
        else:
            eventos = Evento.objects.all().order_by('fecha_inicio')

        context['eventos'] = self.paginate(request, eventos)
        context['qs'] = qs
        
        return context
