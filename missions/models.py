from django.db import models
from django.utils.translation import gettext_lazy as _


class Mission(models.Model):
    driver = models.ForeignKey(to='drivers.Driver', on_delete=models.CASCADE, verbose_name=_('راننده'))
    done = models.BooleanField(default=False, verbose_name=_('انجام شده'), help_text='درحال انجام یا انجام شده')

    class Meta:
        verbose_name = _('ماموریت')
        verbose_name_plural = _('ماموریت ها')

    def __str__(self) -> str:
        return f'{self.driver}'
