from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from users.models import User, Student, Teacher


@register(User)
class UserTransOptions(TranslationOptions):
    # fields = (, )
    pass


@register(Student)
class StudentOptions(TranslationOptions):
    pass


@register(Teacher)
class TeacherOption(TranslationOptions):
    pass
