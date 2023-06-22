from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import *


class MissionsView(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Mission.objects.all()
        return Mission.objects.filter(driver__user=user)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return MissionGetSerializer
        return MissionSerializer
