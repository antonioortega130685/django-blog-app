from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Entrada

# Create your views here.

class IndexView(ListView):

	template_name = 'index.html'
	model = Entrada
	queryset = Entrada.objects.all().order_by('-pub_date')



class EntradaDetailView(DetailView):

	template_name = 'entrada_detail.html'
	model = Entrada

class AboutView(TemplateView):

	template_name = 'about.html'
	model = Entrada