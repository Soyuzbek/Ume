from django.contrib import admin
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from users.forms import MessageForm
from users.models import User, Student, Teacher


def send_message(modeladmin, request, queryset):
    form = None

    if 'cancel' in request.POST:
        modeladmin.message_user(request, 'The action is canceled')
        return HttpResponseRedirect(request.get_full_path())
    elif 'send' in request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            receiver_list = []
            for user in queryset:
                if hasattr(user, 'email'):
                    if user.email is not None and user.email != '':
                        receiver_list.append(user.email)
                if hasattr(user, 'user'):
                    if user.user.email is not None and user.user.email != '':
                        receiver_list.append(user.user.email)
            subject, from_email, to = form.cleaned_data.get('subject'), 'noreply.leti.kg@gmail.com', receiver_list
            text_content = 'This is an important message.'
            html_content = form.cleaned_data.get('message')
            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            if len(receiver_list) == 1:
                modeladmin.message_user(request, _(
                    f"Mail sent successfully for selected {modeladmin.model._meta.verbose_name.title()}"))
            else:
                modeladmin.message_user(request, _(f"""Mail sent successfully for {len
                (receiver_list)} {modeladmin.model._meta.verbose_name_plural.title()}"""))
            return HttpResponseRedirect(request.get_full_path())
    if not form:
        form = MessageForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME),
                                    'action': request.POST['action']})

    return render(request, 'admin/send_mass_mail.html', locals())


send_message.short_description = _('send email')


class StudentAdmin(TranslationStackedInline):
    model = Student


@admin.register(User)
class UserAdmin(TabbedTranslationAdmin):
    fieldsets = ((None, {'fields': ('id', 'email', 'username', 'is_teacher', 'is_student')}),)
    fieldsets += (_('Permissions'), {
        'fields': ('is_active', 'is_staff', 'is_superuser'),
    }),
    inlines = [StudentAdmin]
    actions = [send_message]


@admin.register(Student)
class StudentAdmin(TabbedTranslationAdmin):
    actions = [send_message]
    exclude = None


@admin.register(Teacher)
class TeacherAdmin(TabbedTranslationAdmin):
    actions = [send_message]
    exclude = None
