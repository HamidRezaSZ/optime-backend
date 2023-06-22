from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Mission(models.Model):
    description = models.TextField(verbose_name=_('توضیحات'))
    driver = models.ForeignKey(to='drivers.Driver', on_delete=models.CASCADE,
                               verbose_name=_('راننده'), null=True, blank=True)
    origin_longitude = models.FloatField(default=0, verbose_name=_('طول جغرافیایی مبدا'))
    origin_latitude = models.FloatField(default=0, verbose_name=_('عرض جغرافیایی مبدا'))
    destination_longitude = models.FloatField(default=0, verbose_name=_('طول جغرافیایی مقصد'))
    destination_latitude = models.FloatField(default=0, verbose_name=_('عرض جغرافیایی مقصد'))
    done = models.BooleanField(default=False, verbose_name=_('انجام شده'), help_text='درحال انجام یا انجام شده')

    class Meta:
        verbose_name = _('ماموریت')
        verbose_name_plural = _('ماموریت ها')

    def __str__(self) -> str:
        return f'{self.driver}'

    def clean(self) -> None:
        if not self.pk:
            if self.driver and not self.driver.free:
                raise ValidationError(_('هر راننده در هر لحظه فقط میتواند یک ماموریت در حال انجام داشته باشد'))

        return super().clean()
