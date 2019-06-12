from django.shortcuts import render
from django.views.generic import TemplateView


class Homepage(TemplateView):
	template_name = 'website/index.html'


class About(TemplateView):
	template_name = 'website/about-wealthykate.html'



