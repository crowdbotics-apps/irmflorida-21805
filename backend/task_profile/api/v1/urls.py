from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CustomerProfileViewSet,
    InviteCodeViewSet,
    NotificationViewSet,
    TaskerProfileViewSet,
)

router = DefaultRouter()
router.register("taskerprofile", TaskerProfileViewSet)
router.register("invitecode", InviteCodeViewSet)
router.register("notification", NotificationViewSet)
router.register("customerprofile", CustomerProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
