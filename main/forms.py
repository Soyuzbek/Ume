from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import TextInput, PasswordInput

from main.models import Lesson
from users.models import User, Student


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email' ) #''last_name', 'phone', 'email', 'password', 'address')
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

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.lessons.add(*self.cleaned_data.get('lessons'))
        return user
