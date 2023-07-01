from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import BaseColor, ShadeColor, Palette
from django.views import View

# Create your views here.

class Home(TemplateView):
    model = BaseColor
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["base_colors"] = BaseColor.objects.all()
        return context

class BaseColorList(TemplateView):
    template_name = "base_color_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["base_colors"] = BaseColor.objects.all()
        return context

class BaseDetail(DetailView):
    model = BaseColor
    template_name = 'base_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["shades"] = ShadeColor.objects.filter(base_color=self.kwargs['pk'])
    #     return context