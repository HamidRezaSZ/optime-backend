from django.db import models
from django.utils.translation import gettext_lazy as _


class Driver(models.Model):
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE, verbose_name=_('user'))
    longitude = models.FloatField(default=0, verbose_name=_('طول جغرافیایی'))
    latitude = models.FloatField(default=0, verbose_name=_('عرض جغرافیایی'))
    free = models.BooleanField(default=True, verbose_name=_('آزاد'), help_text='درحال انجام ماموریت یا آزاد')

    class Meta:
        verbose_name = _('راننده')
        verbose_name_plural = _('راننده ها')

    def __str__(self) -> str:
        return f'{self.user}'
