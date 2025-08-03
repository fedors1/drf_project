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


class Mileage(models.Model):
    """ Модель 'Пробег' """
    car = models.ForeignKey(to=CarsList, on_delete=models.CASCADE, null=True, blank=True, related_name="mileage")
    moto = models.ForeignKey(to=MotoList, on_delete=models.CASCADE, null=True, blank=True, related_name="mileage")
    mileage = models.PositiveIntegerField(verbose_name="Пробег")
    year = models.PositiveSmallIntegerField(verbose_name="Год регистрации")

    def __str__(self):
        return f"{self.moto if self.moto else self.car} - {self.year}"

    class Meta:
        verbose_name = "пробег"
        verbose_name_plural = "пробег"
        ordering = ("-year", )
