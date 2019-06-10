from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from main.models import Wallpaper, Post, Lesson


class LanguageView(View):

    def get(self, request, lang):
        request.session['_language'] = lang
        print(request.session['_language'])
        return redirect(request.META.get('HTTP_REFERER', '/'))


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        wallpaper_list = Wallpaper.objects.all()
        advantage_list = Post.objects.filter(name='advantage').first()
        return render(request, self.template_name, locals())


class LessonsView(ListView):
    model = Lesson
    template_name = 'lessons.html'


class LessonItemView(DetailView):
    model = Lesson
    template_name = 'les_item.html'

