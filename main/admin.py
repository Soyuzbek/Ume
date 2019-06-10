from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from main.models import Post, Notification, Lesson, Wallpaper
# from users.models import Student, StudentLesson


#
# class StudentAdmin(admin.StackedInline):
#     model = Student
from users.models import Student


class StudLesson(admin.TabularInline):
    model = Student.lessons.through
    extra = 1


@admin.register(Post)
class PostAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Notification)
class NotAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(TabbedTranslationAdmin):
    inlines = [StudLesson]
    pass


@admin.register(Wallpaper)
class WallAdmin(admin.ModelAdmin):
    pass
