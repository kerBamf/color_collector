from django.shortcuts import render
from django.shortcuts import redirect
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

class AllColors(TemplateView):
    template_name = 'all_colors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_colors"] = ShadeColor.objects.all()
        return context

class ColorCreate(View):
    def post(self, request):
        name = request.POST.get('colorName')
        rgb = request.POST.get('colorRGB')
        hex = request.POST.get('colorHex')
        base_select = request.POST.get('baseSelect')
        redir = request.POST.get('redirect')
        base_color = BaseColor.objects.get(pk=base_select)
        ShadeColor.objects.create(name=name, rgb=rgb, hex=hex, base_color=base_color)
        return redirect(redir)

class ColorUpdate(View):
    def post(self, request, shade_pk):
        name = request.POST.get('colorName')
        rgb = request.POST.get('colorRGB')
        hex = request.POST.get('colorHex')
        base_select = request.POST.get('baseSelect')
        redir = request.POST.get('redirect')
        base_color = BaseColor.objects.get(pk=base_select)
        ShadeColor.objects.filter(pk=shade_pk).update(name=name, rgb=rgb, hex=hex, base_color=base_color)
        return redirect(redir)
    
class FromBaseShadeDelete(View):
    def post(self, request, shade_pk):
        redir = request.POST.get('redirect')
        ShadeColor.objects.filter(pk=shade_pk).delete()
        return redirect(redir)