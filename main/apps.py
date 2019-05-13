from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MainConfig(AppConfig):
    name = _('main')
    verbose_name = _('main')

    def __repr__(self):
        return _('main')
