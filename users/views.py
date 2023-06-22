from rest_framework.generics import CreateAPIView

from .serializers import *


class Register(CreateAPIView):
    serializer_class = UserSerializer
