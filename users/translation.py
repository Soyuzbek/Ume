from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from users.models import User


@register(User)
class UserTransOptions(TranslationOptions):
    # fields = (, )
    pass
