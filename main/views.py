from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from main.models import Wallpaper, Post


class LanguageView(View):

    def get(self, request, lang):
        request.session['_language'] = lang
        print(request.session['_language'])
        return redirect(request.META.get('HTTP_REFERER', '/'))


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        wallpaper_list = Wallpaper.objects.all()
        advantage_list = Post.objects.filter(name='advantage').first()
        return render(request, 'index.html', locals())
