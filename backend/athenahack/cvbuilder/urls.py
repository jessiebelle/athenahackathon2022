from django.db import router
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CVFinishedViewSet, CVQuestionsViewSet, CVViewSet

app_name = "cvbuilder"

router = DefaultRouter()
router.register(r"CV", CVFinishedViewSet, basename="viewcv")
router.register(
    r"CV-questions", CVQuestionsViewSet, basename="questions"
),
router.register(r"cv/create", CVViewSet, basename="create-r1"),

urlpatterns = router.urls