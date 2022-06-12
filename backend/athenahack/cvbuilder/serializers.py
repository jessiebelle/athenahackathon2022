from .models import (
    CV, Experience, UserSkill, User)
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    email = serializers.CharField(style={'base_template': 'textarea.html'})

    class Meta:

        model = User
        fields = ("id", "user", "name", "email")


class CVSerializers:
    class CVSerializer(serializers.ModelSerializer):
        insight_question = serializers.SerializerMethodField()

        class Meta:
            model = CV
            fields = ("id", "user",)

    class CVResponseSerializer(serializers.ModelSerializer):
        user = serializers.SerializerMethodField()


        class Meta:
            model = User
            fields = (
                "user",
                "id",
            )

        def get_work_experience(self, user):
            work_experience = Experience.objects.filter(user=user)
            return work_experience


        def get_user(self, user):
            user = user
            return user

        def get_skills(self, user):
            skills = UserSkill.objects.filter(
                user=user
            )
            return skills

    class CVCreateSerializerR1(serializers.ModelSerializer):
        type_id = serializers.IntegerField(source="annotation_type_id")
        content = serializers.CharField(source="content")

        class Meta:
            model = CV
            fields = (
                "user",
            )

        def create(self, validated_data):
            user = self.context["request"].user
            validated_data["client_id"] = user.company


            return super().create(validated_data)