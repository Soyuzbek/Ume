from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    name = models.CharField(_('name'), max_length=255)
    annotation = models.TextField(_('annotation'))
    content = RichTextUploadingField(verbose_name=_('content'))
    author = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, verbose_name=_('author'))
    date = models.DateTimeField(_('date'), auto_now=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.name


class Notification(models.Model):
    name = models.TextField(_('name'))
    content = RichTextUploadingField(verbose_name=_('content'))
    date = models.DateTimeField(_('date'), auto_now=True)
    expire = models.DateTimeField(_('date of expire'))

    class Meta:
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    id = models.CharField('ID', max_length=7, primary_key=True)
    name = models.CharField(_('name'), max_length=255)
    teacher = models.ForeignKey('users.Teacher', on_delete=models.SET_NULL, null=True, verbose_name=_('teacher'),
                                related_name='lessons')
    STATE_CHOICES = (
        ('ZD', _('Necessary')),
        ('SD', _('Optional'))
    )
    state = models.CharField(_('type'), max_length=5, choices=STATE_CHOICES)
    term = models.PositiveSmallIntegerField(_('term'), default=1)
    topics = RichTextUploadingField(verbose_name=_('topics'), null=True, blank=True)

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def __str__(self):
        return f'{self.id} - {self.name}'

    def get_absolute_url(self):
        return reverse('lesson', args=[str(self.id)])


class Wallpaper(models.Model):
    name = models.CharField(_('name'), max_length=200)
    image = models.ImageField(_('image'), upload_to='image')

    class Meta:
        verbose_name = _('Wallpaper')
        verbose_name_plural = _('Wallpapers')

    def __str__(self):
        return self.name


class Assign(models.Model):
    DAY_CHOICE = (
        ('Monday', _('Monday')),
        ('Tuesday', _('Tuesday')),
        ('Wednesday', _('Wednesday')),
        ('Thursday', _('Thursday')),
        ('Friday', _('Friday')),
    )
    TIME_SLOTS = (
        ('8:00 - 8:45', '8:00 - 8:45'),
        ('8:55 - 9:40',  '8:55 - 9:40'),
        ('9:50 - 10:35', '9:50 - 10:35'),
        ('10:45 - 11:30', '10:45 - 11:30'),
        ('11:40 - 12:25', '11:40 - 12:25'),
        ('12:35 - 13:20', '12:35 - 13:20'),
        ('13:30 - 14:15', '13:30 - 14:15'),
        ('14:25 - 15:10', '14:25 - 15:10'),
        ('15:20 - 16:05', '15:20 - 16:05'),
        ('16:15 - 17:00', '16:15 - 17:00'),
        ('17:10 - 17:55', '17:10 - 17:55')
    )
    ROOM_CHOICES = (
        ('101', '101'),
        ('102', '102'),
        ('103', '103'),
        ('104', '104'),
        ('105', '105'),
        ('106', '106'),
        ('107', '107'),
        ('118', '118'),
        ('119', '119')
    )
    lesson = models.ForeignKey(Lesson, models.CASCADE, related_name='assign_set', verbose_name=_('lesson'))
    room = models.CharField(_('room'), max_length=10, choices=ROOM_CHOICES)
    day = models.CharField(_('day'), max_length=15, choices=DAY_CHOICE)
    time_slots = models.CharField(_('time slot'), max_length=13, choices=TIME_SLOTS, default=TIME_SLOTS[0])

    class Meta:
        verbose_name = _('Assign')
        verbose_name_plural = _('Assigns')
