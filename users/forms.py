from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.admin.helpers import ActionForm
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import TextInput, PasswordInput

from main.models import Lesson
from users.models import User, Student


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('id', 'username', 'email' ) #''last_name', 'phone', 'email', 'password', 'address')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            # 'last_name': TextInput(attrs={'class': 'form-control'}),
            # 'phone': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            # 'password': PasswordInput(attrs={'class': 'form-control'}),
            # 'address': TextInput(attrs={'class': 'form-control'})
        }


class StudentSignUpForm(UserCreationForm):
    lessons = forms.ModelMultipleChoiceField(
        queryset=Lesson.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('id', 'username', 'is_staff')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.lessons.add(*self.cleaned_data.get('lessons'))
        return user


# class StudentLoginForm(forms.UserLoginForm):
#
#     class Meta:
#         model = User
#         fields = ('id',  'password')


class StudentLoginForm(forms.ModelForm):
    next = forms.CharField(widget=TextInput(attrs={'hidden': True}), required=False)

    class Meta:
        model = User
        fields = ('id', 'password', 'next')
        widgets = {
            'id': TextInput(attrs={'class': 'form-control', 'placeholder': 'id'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'})
        }


class MessageForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=CKEditorWidget())
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    action = forms.CharField(widget=forms.HiddenInput)