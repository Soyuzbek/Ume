from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from users.models import User, Student, Teacher


@register(User)
class UserTransOptions(TranslationOptions):
    fields = ('username', )
    pass


@register(Student)
class StudentOptions(TranslationOptions):
    fields = ('father', 'mother', 'address', 'home_address')


@register(Teacher)
class TeacherOption(TranslationOptions):
    pass
