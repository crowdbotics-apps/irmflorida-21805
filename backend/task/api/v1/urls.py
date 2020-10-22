from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import MessageViewSet, RatingViewSet, TaskViewSet, TaskTransactionViewSet

router = DefaultRouter()
router.register("rating", RatingViewSet)
router.register("tasktransaction", TaskTransactionViewSet)
router.register("message", MessageViewSet)
router.register("task", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
