from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
   email = models.EmailField(verbose_name="Почта", unique=True)
   phone_number = models.CharField(max_length=15, verbose_name="Номер телефона", blank=True, null=True)
   city = models.CharField(verbose_name="Город", blank=True, null=True)
   avatar = models.ImageField(verbose_name="Аватарка", upload_to="images/users/photo/", default="images/users/photo/default.png")

   USERNAME_FIELD = "email"
   REQUIRED_FIELDS = ["username", ]

   def __str__(self):
       return self.email
