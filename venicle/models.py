from django.db import models


# Create your models here.
class CarsList(models.Model):
    """Список машин"""

    title = models.CharField(max_length=50, verbose_name="Модель автомобиля")
    description = models.TextField(verbose_name="Описание автомобиля")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"


class MotoList(models.Model):
    """Список машин"""

    title = models.CharField(max_length=50, verbose_name="Модель мотоцикла")
    description = models.TextField(verbose_name="Описание мотоцикла")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мотоцикл"
        verbose_name_plural = "Мотоциклы"
