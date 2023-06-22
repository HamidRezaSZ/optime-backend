from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from drivers.serializers import DriverGetSerializer

from .models import *
from .utils import nearest_driver


class MissionSerializer(serializers.ModelSerializer):
    auto_assign = serializers.BooleanField(default=False, write_only=True, required=False)

    class Meta:
        model = Mission
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('driver') and not attrs['driver'].free:
            raise serializers.ValidationError(
                {'راننده': _('هر راننده در هر لحظه فقط میتواند یک ماموریت در حال انجام داشته باشد')})

        return super().validate(attrs)

    def create(self, validated_data):
        if validated_data.get('auto_assign'):
            validated_data['driver'] = nearest_driver(
                validated_data['origin_longitude'],
                validated_data['origin_latitude'])
            validated_data.pop('auto_assign')

        return super().create(validated_data)


class MissionGetSerializer(serializers.ModelSerializer):
    driver = DriverGetSerializer()

    class Meta:
        model = Mission
        fields = '__all__'
