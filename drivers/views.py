from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .serializers import *


class DriversView(ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Driver.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return DriverGetSerializer
        return DriverSerializer
