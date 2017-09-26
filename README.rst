Blog20

Blog20 es un prototipo simple de app Django de blog en la Web.

Inicio rápido

1.Agregue las siguientes apps a su configuración INSTALLED_APPS como sigue:

INSTALLED_APPS = [
    ...
    'blog20',
    'ckeditor',
    'ckeditor_uploader',
]

2.Incluya el URLconf de blog en su proyecto urls.py como sigue:

from django.conf.urls import url, include
from django.contrib import admin
from blog20.views import IndexView, EntradaDetailView, AboutView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^entrada/(?P<slug>[-\w]+)/$', EntradaDetailView.as_view(), name='detail'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^about/', AboutView.as_view(), name='about'),

]

3.Corra python manage.py migrate para crear los modelos de polls.

4.Corra python manage.py collectstatic.

5.Cruce los dedos.

6.Arranque el servidor de desarrollo y visite http://127.0.0.1:8000/admin/ para crear y administrar sus posteos (va a necesitar la app Admin habilitada). Utilice el usuario 'usuario' y la contraseña 'proyecto'.

7.Visite http://127.0.0.1:8000/ para ver el blog.