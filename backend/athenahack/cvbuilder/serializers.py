from rest_framework import serializers

from athenahackathon2022.backend.athenahack.cvbuilder.models import CV, UserSkill, Experience


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
            model = CV
            fields = (
                "id",
                "client",
                "user",
                "user_public_id",
                "user_deleted",
                "user_fullname",
                "user_insight_response",
                "is_anon",
                "course_section",
                "course_section_title",
                "course_section_url_slug",
                "course_page_no",
                "course_page_title",
                "course_page_url_slug",
                "insight_question",
                "admin_responded",
                "created",
                "archived",
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

