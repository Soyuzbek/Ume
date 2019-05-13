from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from django.utils.translation import gettext_lazy as _

from users.models import User


@admin.register(User)
class StudentAdmin(TabbedTranslationAdmin):
    fieldsets = ((None, {'fields': ('id', 'username', 'password', )}),
                 (_('Personal info'), {'fields': ('is_student', 'is_teacher')}))

