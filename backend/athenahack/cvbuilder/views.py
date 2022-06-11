from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.viewsets import ReadOnlyModelViewSet


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class CViewSetR1(ReadOnlyModelViewSet):
    queryset = InsightQuestion.objects.all()
    serializer_class = InsightSerializers.InsightQuestionSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering = ("insight_question",)

    def get_queryset(self):
        return InsightQuestion.objects.filter_by_user(user=self.request.user)

    @translation_wrapper
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response