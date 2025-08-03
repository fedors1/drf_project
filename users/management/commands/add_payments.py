from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import User, Payments


class Command(BaseCommand):

    help = "Add test payments to the database"

    def handle(self, *args, **options):
        user, _ = User.objects.get_or_create(email="test-user@email.ru")

        course1 = Course.objects.create(
            name="Курсы по математике",
            description="Базовая подготовка по математике",
            preview="images/materials/courses/photo/default.png",
        )
        course2 = Course.objects.create(
            name="Курсы по русскому языку",
            description="Базовая подготовка по русскому языку",
            preview="images/materials/courses/photo/default.png",
        )
        lesson1 = Lesson.objects.create(
            name="Квадратный корень",
            description="Вычисление квадратного корня",
            preview="images/materials/lessons/photo/default.png",
            link_to_the_video="https://1234",
            course=course1,
        )
        lesson2 = Lesson.objects.create(
            name="Глаголы",
            description="Закрепление знаний по глаголам",
            preview="images/materials/lessons/photo/default.png",
            link_to_the_video="https://12345",
            course=course2,
        )

        payments = [
            {
                "user": user,
                "date_payment": "2024-12-12 22:23:21",
                "payment_lesson": lesson1,
                "payment_course": course1,
                "payment": 9999,
                "payment_method": Payments.CASH2,
            },
            {
                "user": user,
                "date_payment": "2021-11-11 11:13:09",
                "payment_lesson": lesson1,
                "payment_course": course1,
                "payment": 91999,
                "payment_method": Payments.CASH1,
            },
            {
                "user": user,
                "date_payment": "2023-10-01 09:53:30",
                "payment_lesson": lesson2,
                "payment_course": course2,
                "payment": 8888,
                "payment_method": Payments.CASH1,
            },
            {
                "user": user,
                "date_payment": "2020-07-03 07:53:39",
                "payment_lesson": lesson2,
                "payment_course": course2,
                "payment": 98907,
                "payment_method": Payments.CASH2,
            },
        ]

        for payment in payments:
            payment, created = Payments.objects.get_or_create(**payment)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"successfully added payment: {payment.user}, {payment.date_payment}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Payment already exist: {payment.user}, {payment.date_payment}")
                )
