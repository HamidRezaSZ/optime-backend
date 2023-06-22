from django.db.models import ExpressionWrapper, F, FloatField

from drivers.models import Driver


def nearest_driver(origin_longitude, origin_latitude):
    return Driver.objects.filter(
        free=True).annotate(
        diff=ExpressionWrapper(
            ((origin_longitude - F('longitude')) ** 2) + ((origin_latitude - F('latitude')) ** 2),
            output_field=FloatField())).order_by('diff').first()
