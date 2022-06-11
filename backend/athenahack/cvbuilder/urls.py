from django.db import router
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import CVViewSet, CVFinishedViewSet, CVQuestionsViewSet

app_name = "insights"

router = DefaultRouter()
router.register(r"CV/", CVFinishedViewSet, basename="r1")
router.register(
    r"CV-questions/", CVQuestionsViewSet, basename="questions"
),
router.register(r"cv/create/", CVViewSet, basename="create-r1"),

urlpatterns = router.urls