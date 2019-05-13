from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    id = models.CharField(_('ID'), max_length=10, primary_key=True)
    is_teacher = models.BooleanField(_('is teacher'), default=False)
    is_student = models.BooleanField(_('is student'), default=False)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Teacher(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name='teacher_profile', primary_key=True)
    degree = models.CharField(_('degree'), max_length=200)
    status = models.CharField(_('degree'), max_length=200)
    GROUP_CHOICES = (
        ('UME-I', _('First course')),
        ('UME-II', _('Second course')),
        ('UME-III', _('Third course')),
        ('UME-IV', _('Fourth course'))
    )
    own_group = models.CharField(_('own group'), max_length=7, choices=GROUP_CHOICES, default='UME-I')
    lessons = models.ManyToManyField('main.Lesson', 'lesson_list')
    phone_regex_kg = RegexValidator(regex=r'^\+?996?\d{9,15}$',
                                    message=_("Phone number must be entered in the format:"
                                              " '+996999999'. Up to 15 digits allowed"))
    phone_regex_tr = RegexValidator(regex=r'^\+?90\d{10, 12}$',
                                    message=_('Please type in the correct format.'))
    phone = models.CharField(verbose_name=_('phone'), max_length=15, validators=[phone_regex_kg, phone_regex_tr])
    father = models.CharField(verbose_name=_('father'), max_length=55)
    mother = models.CharField(verbose_name=_('mother'), max_length=55)
    address = models.TextField(_('address'))
    home_address = models.TextField(_('home address'))

    @staticmethod
    def get_absolute_url():
        return f'/users/user/{1}'


class Student(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name='student_profile', primary_key=True)
    COURSE_CHOICES = (
        ('UME-I', _('First course')),
        ('UME-II', _('Second course')),
        ('UME-III', _('Third course')),
        ('UME-IV', _('Fourth course'))
    )
    course = models.CharField(_('course'), max_length=7, choices=COURSE_CHOICES, default='UME-I')
    curator = models.ForeignKey('Teacher', models.DO_NOTHING, verbose_name=_('curator'))
    lessons = models.ManyToManyField('main.Lesson', 'student_list')
    phone_regex_kg = RegexValidator(regex=r'^\+?996?\d{9,15}$',
                                    message=_("Phone number must be entered in the format:"
                                              " '+996999999'. Up to 15 digits allowed"))
    phone_regex_tr = RegexValidator(regex=r'^\+?90\d{10, 12}$',
                                    message=_('Please type in the correct format.'))
    phone = models.CharField(verbose_name=_('phone'), max_length=15, validators=[phone_regex_kg, phone_regex_tr])
    father = models.CharField(verbose_name=_('father'), max_length=55)
    mother = models.CharField(verbose_name=_('mother'), max_length=55)
    address = models.TextField(_('address'))
    home_address = models.TextField(_('home address'))

    class Meta(AbstractUser.Meta):
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    # @staticmethod
    # def get_absolute_url():
    #     return ''
