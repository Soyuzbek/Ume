from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from main.models import Post, Notification, Lesson, Wallpaper, Assign

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


@admin.register(Assign)
class AssignAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'room', 'day', 'time_slots')
    list_editable = ('lesson', 'room', 'day', 'time_slots')
