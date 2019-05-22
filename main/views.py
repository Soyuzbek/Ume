from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView

from main.forms import StudentSignUpForm
from main.models import Wallpaper, Post
from users.models import User


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


class SignUpView(View):
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('')


class TeacherSignUpView(CreateView):
    pass
