from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    BusinessPhotoViewSet,
    TaskerAvailabilityViewSet,
    TaskerSkillViewSet,
    TimeslotViewSet,
)

router = DefaultRouter()
router.register("timeslot", TimeslotViewSet)
router.register("taskeravailability", TaskerAvailabilityViewSet)
router.register("taskerskill", TaskerSkillViewSet)
router.register("businessphoto", BusinessPhotoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
