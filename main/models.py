from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    name = models.CharField(_('name'), max_length=255)
    annotation = models.TextField(_('annotation'))
    content = RichTextField()
    author = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    date = models.DateTimeField(_('date'), auto_now=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.name


class Notification(models.Model):
    name = models.TextField(_('name'))
    content = RichTextField()
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
    STATE_CHOICES = (
        ('ZD', _('Necessary')),
        ('SD', _('Optional'))
    )
    state = models.CharField(verbose_name=_('type'), max_length=5, choices=STATE_CHOICES)
    term = models.PositiveSmallIntegerField(verbose_name=_('term'), default=1)

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def __str__(self):
        return self.name


class Wallpaper(models.Model):
    name = models.CharField(_('name'), max_length=200)
    image = models.ImageField(_('image'), upload_to='image')

    class Meta:
        verbose_name = _('Wallpaper')
        verbose_name_plural = _('Wallpapers')

    def __str__(self):
        return self.name
