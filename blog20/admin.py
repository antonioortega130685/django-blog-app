from django.contrib import admin
from .models import Entrada


# Register your models here.

class EntradaAdmin(admin.ModelAdmin):
    fieldsets = [
    	('User information', {'fields': ['user']}),
        (None,               {'fields': ['titulo']}),
        (None,               {'fields': ['subtitulo']}),
        (None, {'fields':['contenido']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('titulo', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Entrada, EntradaAdmin)
