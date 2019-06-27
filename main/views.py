from urllib.parse import unquote

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView

from main.models import Wallpaper, Post, Lesson, Assign
from users.models import Teacher


class LanguageView(View):

    def get(self, request, lang):
        request.session['_language'] = lang
        print(request.session['_language'])
        return redirect(request.META.get('HTTP_REFERER', '/'))


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        wallpaper = Wallpaper.objects.first()
        about = Post.objects.filter(name='About us').first()
        advantage = Post.objects.filter(name='Your advantages').first()
        rooms = Assign.ROOM_CHOICES
        teachers = Teacher.objects.all()
        return render(request, self.template_name, locals())


class AdvantageView(View):
    template_name = 'blog.html'

    def get(self, request):
        advantage = Post.objects.filter(name='Your advantages').first()
        return render(request, self.template_name, locals())


class AboutView(View):
    template_name = 'about.html'

    def get(self, request):
        about = Post.objects.filter(name='About').first()
        return render(request, self.template_name, locals())


class LessonsView(ListView):
    model = Lesson
    template_name = 'lessons.html'


class LessonItemView(DetailView):
    model = Lesson
    template_name = 'les_item.html'


class TimetableView(View):
    model = Assign
    template_name = 'timetable.html'

    def get(self, request, slug):
        asst = Assign.objects.all()
        class_matrix = [[True for i in range(12)] for j in range(5)]
        time_slots = Assign.TIME_SLOTS
        if slug == 'by_room':
            rooms = Assign.ROOM_CHOICES
        elif slug == 'by_teacher':
            teachers = Teacher.objects.all()
        else:
            lessons = Lesson.objects.all()
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
        return render(request, self.template_name, locals())


class RoomTable(View):
    model = Assign
    template_name = 'timetable.html'

    def get(self, request, room):
        asst = Assign.objects.filter(room=room)
        class_matrix = [[ True for i in range(12)] for j in range(5)]
        time_slots = Assign.TIME_SLOTS
        rooms = Assign.ROOM_CHOICES
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
        return render(request, self.template_name, locals())


class SelfTable(View):
    model = Assign
    template_name = 'timetable.html'

    @method_decorator(login_required)
    def get(self, request):
        if hasattr(request.user, 'student_profile'):
            lessons = Lesson.objects.filter(student_list=request.user.student_profile)
            asst = Assign.objects.filter(lesson__in=lessons)

        else:
            lessons = Lesson.objects.filter(teacher=request.user.teacher_profile)
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
        return render(request, self.template_name, locals())


class TeacherTable(View):
    model = Assign
    template_name = 'timetable.html'

    def get(self, request, slug):
        teachers = Teacher.objects.all()
        lessons = Lesson.objects.filter(teacher__user__username=unquote(slug))
        asst = Assign.objects.filter(lesson__in=lessons)
        del lessons
        class_matrix = [[ True for i in range(12)] for j in range(5)]
        time_slots = Assign.TIME_SLOTS
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
        return render(request, self.template_name, locals())


class LessonTable(View):
    model = Assign
    template_name = 'timetable.html'

    def get(self, request, id):
        lessons = Lesson.objects.all()
        asst = Assign.objects.filter(lesson__id=id)
        class_matrix = [[True for i in range(12)] for j in range(5)]
        time_slots = Assign.TIME_SLOTS
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
        return render(request, self.template_name, locals())
