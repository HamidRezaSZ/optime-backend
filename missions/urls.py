from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'missions', MissionsView, basename='mission')

urlpatterns = router.urls
