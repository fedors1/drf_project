from rest_framework import serializers

from materials.models import Lesson, Course
from users.models import Payments


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    @staticmethod
    def get_lesson_count(instance):
        return instance.lessons.count()

    class Meta:
        model = Course
        fields = ["name", "description", "preview", "lesson_count", "lessons"]


class PaymentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Payments
        fields = [
            "user",
            "date_payment",
            "payment_lesson",
            "payment_course",
            "payment",
            "payment_method",
            "courses",
        ]