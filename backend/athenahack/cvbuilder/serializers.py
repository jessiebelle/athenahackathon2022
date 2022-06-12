from .models import (
    CV, Experience, UserSkill, User)
from rest_framework import serializers


class CVSerializers:
    class CVSerializer(serializers.ModelSerializer):
        insight_question = serializers.SerializerMethodField()

        class Meta:
            model = CV
            fields = ("id", "type_name", "insight_question")

        def get_insight_question(self, annotation_type):
            insight_question = annotation_type.translate.insight_question

            return insight_question

    class CVResponseSerializer(serializers.ModelSerializer):
        user = serializers.SerializerMethodField()
        user_public_id = serializers.SerializerMethodField()
        user_deleted = serializers.SerializerMethodField()
        user_fullname = serializers.SerializerMethodField()


        class Meta:
            model = User
            fields = (
                "user_id",
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
        content = serializers.CharField(source="insight_content")

        class Meta:
            model = CV
            fields = (
                "user",
            )

        def create(self, validated_data):
            user = self.context["request"].user
            validated_data["client_id"] = user.company


            return super().create(validated_data)