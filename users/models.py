from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    id = models.CharField(_('ID'), max_length=10, primary_key=True)
    is_teacher = models.BooleanField(_('is teacher'), default=False)
    is_student = models.BooleanField(_('is student'), default=False)
    username_validator = RegexValidator(regex=r'^[\w.@+ -]+$', message=_('Enter a valid username. This value may contain only letters,' 
        'numbers, spaces and @/./+/-/_ characters.'))
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = [username, 'email']

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        ordering = ('id', 'username')
    def __str__(self):
        return f'{self.username}'


class Teacher(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name='teacher_profile', primary_key=True, verbose_name=_('user'), to_field='id')
    degree = models.CharField(_('degree'), max_length=200, null=True, blank=True)
    GROUP_CHOICES = (
        ('UME-I', _('First course')),
        ('UME-II', _('Second course')),
        ('UME-III', _('Third course')),
        ('UME-IV', _('Fourth course'))
    )
    own_group = models.CharField(_('own group'), max_length=7, choices=GROUP_CHOICES, null=True, blank=True)
    phone_regex_kg = RegexValidator(regex=r'^\+?996?\d{9,15}$',
                                    message=_("Phone number must be entered in the format:"
                                              " '+996999999'. Up to 15 digits allowed"))
    phone_regex_tr = RegexValidator(regex=r'^\+?90\d{10, 12}$',
                                    message=_('Please type in the correct format.'))
    short_phone_regex_kg = RegexValidator(regex=r'^\0?\d{9,10}$',
                                    message=_("Phone number must be entered in the format:"
                                              " '+996999999'. Up to 15 digits allowed"))
    phone = models.CharField(verbose_name=_('phone'), max_length=15, validators=[phone_regex_kg, phone_regex_tr], null=True, blank=True)
    address = models.TextField(_('address'), null=True, blank=True)

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')
        ordering = ('user', )

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('teach_item', args=[str(self.user.id)])


class Student(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name='student_profile', primary_key=True, verbose_name=_('user'), to_field='id')
    COURSE_CHOICES = (
        ('UME-I', _('First course')),
        ('UME-II', _('Second course')),
        ('UME-III', _('Third course')),
        ('UME-IV', _('Fourth course'))
    )
    course = models.CharField(_('course'), max_length=7, choices=COURSE_CHOICES, null=True, blank=True)
    lessons = models.ManyToManyField('main.Lesson', 'student_list', verbose_name=_('lessons'))
    phone_regex_kg = RegexValidator(regex=r'^\+?996?\d{9,15}$',
                                    message=_("Phone number must be entered in the format:"
                                              " '+996999999'. Up to 15 digits allowed"))
    phone_regex_tr = RegexValidator(regex=r'^\+?90\d{10, 12}$',
                                    message=_('Please type in the correct format.'))
    phone = models.CharField(verbose_name=_('phone'), max_length=15, validators=[phone_regex_kg, phone_regex_tr], null=True, blank=True)
    father = models.CharField(verbose_name=_('father'), max_length=55, null=True, blank=True)
    mother = models.CharField(verbose_name=_('mother'), max_length=55, null=True, blank=True)
    address = models.TextField(_('address'), null=True, blank=True)
    home_address = models.TextField(_('home address'), null=True, blank=True)

    class Meta(AbstractUser.Meta):
        verbose_name = _('Student')
        verbose_name_plural = _('Students')
        ordering = ('user', )

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('stud_item', args=[str(self.user.id)])
