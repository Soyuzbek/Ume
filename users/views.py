from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from main.models import Lesson, Assign
from users.forms import StudentSignUpForm, StudentLoginForm
from users.models import User, Student, Teacher


class SignUpView(View):
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class StudentSignUpView(View):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get(self, request, **kwargs):
        form = StudentSignUpForm()
        return render(request, self.template_name, locals())

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        print('validation of form: ', form.is_valid(), '\n', 'form : ', form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'index.html', {})
        return render(request, self.template_name, {'errors': form.error_messages})


class TeacherSignUpView(View):
    pass


class LogoutView(View):
    def get(self, request, **kwargs):
        logout(request)
        return redirect('home')


class LoginView(View):
    model = User
    form_class = StudentLoginForm
    template_name = 'registration/login.html'

    def get(self, request, **kwargs):
        form = self.form_class({'next': request.GET.get('next', '/')})
        return render(request, self.template_name, locals())

    def post(self, request):
        user = authenticate(id=request.POST.get('id'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            next = request.POST.get('next', '/')
            return redirect(next)
        messages.add_message(request, messages.INFO, request.POST.get('next', '/'))
        return HttpResponseRedirect(reverse('users:sign_up'))


class StudentsView(ListView):
    model = Student
    template_name = 'students.html'
    ordering = 'user'


class StudentItemView(DetailView):
    model = Student
    template_name = 'stud_item.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        lessons = Lesson.objects.filter(teacher=self.slug_field)
        asst = Assign.objects.filter(lesson__in=lessons)
        class_matrix = [[ True for i in range(12)] for j in range(5)]
        time_slots = Assign.TIME_SLOTS
        # rooms = Assign.ROOM_CHOICES
        # teachers = Teacher.objects.all()
        for i, d in enumerate(Assign.DAY_CHOICE):
            t = 0
            for j in range(len(time_slots) + 1):
                if j == 0:
                    class_matrix[i][0] = d[1]
                    continue
                # if j == 4 or j == 8:
                #     continue
                try:
                    a = asst.filter(time_slots=time_slots[t][0], day=d[0])
                    class_matrix[i][j] = a
                except Assign.DoesNotExist:
                    pass
                t += 1
        data['class_matrix'] = class_matrix
        data['time_slots'] = time_slots
        return data

class TeachersView(ListView):
    model = Teacher
    template_name = 'teachers.html'


class TeacherItemView(DetailView):
    model = Teacher
    template_name = 'teach_item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student_list = Student.objects.filter(course=self.object.own_group)
        context['student_list'] = student_list
        return context
