from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from main.models import Post, Notification, Lesson, Wallpaper


@admin.register(Post)
class StudentAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Notification)
class NotAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Wallpaper)
class WallAdmin(admin.ModelAdmin):
    pass
