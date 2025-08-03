from rest_framework import generics
from rest_framework.filters import OrderingFilter

from materials.models import Lesson, Course
from materials.serializers import PaymentSerializer
from users.models import Payments
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


class PaymentsFilter(filters.FilterSet):
    lesson_name = filters.CharFilter(field_name='payment_lesson__name', lookup_expr='icontains')
    course_name = filters.CharFilter(field_name='payment_course__name', lookup_expr='icontains')

    class Meta:
        model = Payments
        fields = ['lesson_name', 'course_name', 'payment_method']


class PaymentsListAPIView(generics.ListAPIView):

    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_class = PaymentsFilter
    ordering_fields = ["date_payment", "course_name", "lesson_name"]