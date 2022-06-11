from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.viewsets import ReadOnlyModelViewSet

from athenahackathon2022.backend.athenahack.cvbuilder.models import CV


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class CVViewSetR1(ReadOnlyModelViewSet):
    queryset = CV.objects.all()
    serializer_class = InsightSerializers.InsightQuestionSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering = ("insight_question",)

    def get_queryset(self):
        return CV.objects.filter_by_user(user=self.request.user)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response