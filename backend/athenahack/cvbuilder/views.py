from django.http import HttpResponse
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import CV
from .serializers import CVSerializers


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class CVViewSet(ReadOnlyModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializers.CVResponseSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering = ("insight_question",)

    def get_queryset(self):
        return CV.objects.filter_by_user(user=self.request.user)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response


class CVFinishedViewSet(ReadOnlyModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializers.CVResponseSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering = ("insight_question",)

    def get_queryset(self):
        return CV.objects.filter_by_user(user=self.request.user)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response


class CVQuestionsViewSet(ReadOnlyModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializers.CVResponseSerializer
    filter_backends = (DjangoFilterBackend,)


    def get_queryset(self):
        return CV.objects.filter_by_user(user=self.request.user)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response


class CVCreateViewSetR1(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    serializer_class = CVSerializers.CVCreateSerializerR1
