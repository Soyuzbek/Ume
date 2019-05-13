from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from main.models import Post, Notification, Lesson, Wallpaper


@register(Post)
class UserTransOptions(TranslationOptions):
    fields = ('name', 'annotation', 'content')


@register(Notification)
class NotTransOptions(TranslationOptions):
    fields = ('name', 'content')


@register(Lesson)
class LessonTransOpion(TranslationOptions):
    fields = ('name', )


