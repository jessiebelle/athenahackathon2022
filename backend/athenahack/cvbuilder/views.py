from django.http import HttpResponse
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import CV, Experience, Skill, AboutMe, User
from .serializers import CVSerializers



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


class ListCV(APIView):

    def get(self, request):
        user = request.user
        user_details = User.objects.filter(user=user)
        about_me = AboutMe.objects.filer(user=user)
        skill = Skill.objects.filter(user=user)
        experience = Experience.objects.filter(user=user)

        serializer = CVSerializers.CVResponseSerializer(user_details, about_me, skill, experience, many=True)
        return Response(serializer.data)


class CVFinishedViewSet(ReadOnlyModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializers.CVResponseSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)

    def get_queryset(self):
        return CV.objects.filter_by_user(user=self.request.user_id)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response

    @action(methods=["get"], detail=True, url_path="cv", url_name="cv")
    def publish(self, request, *args, **kwargs):
        self.serializer_class = CVCreateViewSetR1
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


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
