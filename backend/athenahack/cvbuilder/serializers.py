from rest_framework import serializers

from athenahackathon2022.backend.athenahack.cvbuilder.models import CV


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
        user_insight_response = serializers.CharField(source="insight_content")
        course_section_title = serializers.SerializerMethodField()
        course_section_url_slug = serializers.SerializerMethodField()
        course_page_no = serializers.SerializerMethodField()
        course_page_title = serializers.SerializerMethodField()
        course_page_url_slug = serializers.SerializerMethodField()
        insight_question = serializers.SerializerMethodField()
        admin_responded = serializers.SerializerMethodField()

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

        def get_work_experience(self, insight):
            work_experience = None
            if not insight.is_anon and insight.user:
                fullname = insight.user.get_full_name()
            return fullname

        def get_user_public_id(self, insight):
            public_id = None
            if not insight.is_anon and insight.user:
                public_id = insight.user.public_id
            return public_id

        def get_user(self, insight):
            user = None
            if not insight.is_anon and insight.user:
                user = insight.user.id
            return user

        def get_user_deleted(self, insight):
            user_deleted = None
            if not insight.is_anon and insight.user:
                user_deleted = insight.user.is_archived
            return user_deleted

        def get_insight_question(self, insight):
            question_content = ""
            insight_question_qs = InsightQuestion.objects.filter(
                id=insight.annotation_type.id
            )
            if insight_question_qs.exists():
                question_content = (
                    insight_question_qs.first().translate.insight_question
                )

            return question_content

        def get_admin_responded(self, insight):
            admin_response = None
            try:
                insight_reply = InsightReply.objects.get(insight=insight)
                admin_response = InsightSerializers.InsightAdminListSerializer(
                    insight_reply
                ).data

            except InsightReply.DoesNotExist:
                pass

            return admin_response

        def get_course_section_url_slug(self, insight):
            course_section_slug = None
            if insight.course_section:
                try:
                    course_section_slug = CourseSection.objects.get(
                        published=True, id=insight.course_section.id
                    ).url_slug
                except CourseSection.DoesNotExist:
                    pass

            return course_section_slug

        def get_course_section_title(self, insight):
            course_section_title = None
            if insight.course_section:
                try:
                    course_section_title = CourseSection.objects.get(
                        published=True, id=insight.course_section.id
                    ).translate.section_title
                except CourseSection.DoesNotExist:
                    pass

            return course_section_title

        def get_course_page_no(self, insight):
            course_page_number = 0
            if insight.course_page and insight.course_section:
                pages = list(
                    CoursePage.objects.filter(
                        published=True, course_section_id=insight.course_section.id
                    )
                    .values_list("id", flat=True)
                    .order_by("sort_order")
                )
                try:
                    course_page_number = pages.index(insight.course_page.id) + 1
                except ValueError:
                    pass

            return course_page_number

        def get_course_page_url_slug(self, insight):
            course_page_slug = None
            if insight.course_page:
                try:
                    course_page_slug = CoursePage.objects.get(
                        published=True, id=insight.course_page.id
                    ).url_slug
                except CoursePage.DoesNotExist:
                    pass

            return course_page_slug

        def get_course_page_title(self, insight):
            course_page_title = None
            if insight.course_page:
                try:
                    course_page_title = CoursePage.objects.get(
                        published=True, id=insight.course_page.id
                    ).translate.page_title
                except CoursePage.DoesNotExist:
                    pass

            return course_page_title