from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Lesson, Course


class User(AbstractUser):

   """ Модель 'Пользователь' """

   email = models.EmailField(verbose_name="Почта", unique=True, )
   phone_number = models.CharField(max_length=15, verbose_name="Номер телефона", blank=True, null=True, )
   city = models.CharField(verbose_name="Город", blank=True, null=True, )
   avatar = models.ImageField(
      verbose_name="Аватарка",
      upload_to="images/users/photo/",
      default="images/users/photo/default.png",
   )

   USERNAME_FIELD = "email"
   REQUIRED_FIELDS = ["username", ]

   def __str__(self):
       return self.email

   class Meta:
      verbose_name = "Пользователь"
      verbose_name_plural = "Пользователи"


class Payments(models.Model):

   """ Модель 'Платежи' """

   CASH1 = "Наличные"
   CASH2 = "Перевод на счет"

   CASH_CHOICES = [
      (CASH1, "Наличные"),
      (CASH2, "Перевод на счет"),
   ]


   user = models.ForeignKey(
      to=User,
      on_delete=models.CASCADE,
      blank=True, null=True,
      related_name="users",
      verbose_name="Пользователь",
   )
   date_payment = models.DateTimeField(auto_now_add=True, verbose_name="Дата платежа", )
   payment_lesson = models.ForeignKey(
      to=Lesson,
      on_delete=models.CASCADE,
      related_name="lessons",
      verbose_name="Оплаченный урок",
   )
   payment_course = models.ForeignKey(
      to=Course,
      on_delete=models.CASCADE, related_name="courses",
      verbose_name="Оплаченный курс",
   )
   payment = models.PositiveIntegerField(default=0, verbose_name="Сумма оплаты", )
   payment_method = models.CharField(max_length=16, choices=CASH_CHOICES, verbose_name="Способ оплаты", )

   def __str__(self):
      return f"Информация по оплате для пользователя: {self.user} - {self.payment_lesson}, {self.payment_course}"

   class Meta:
      verbose_name = "Платеж"
      verbose_name_plural = "Платежи"
