from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from drivers.serializers import DriverGetSerializer

from .models import *


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('driver') and not attrs['driver'].free:
            raise serializers.ValidationError(
                {'راننده': _('هر راننده در هر لحظه فقط میتواند یک ماموریت در حال انجام داشته باشد')})

        return super().validate(attrs)


class MissionGetSerializer(serializers.ModelSerializer):
    driver = DriverGetSerializer()

    class Meta:
        model = Mission
        fields = '__all__'
