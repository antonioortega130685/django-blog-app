from django.db import models
from django.conf import settings
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField



# Create your models here.
class Entrada(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    titulo = models.CharField(max_length = 200)
    subtitulo = models.CharField(max_length = 200)
    contenido = RichTextField()
    slug = models.SlugField(editable = False)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.titulo
    

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Entrada, self).save(*args, **kwargs)