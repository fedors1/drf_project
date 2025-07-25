from django.db import models

# Create your models here.
class Course(models.Model):

    """ Модель 'Course' """

    name = models.CharField(max_length=100, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание курса")
    preview = models.ImageField(
        verbose_name="Картинка",
        upload_to="images/materials/courses/photo/",
        default="images/materials/courses/photo/default.png"
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):

    """ Модель 'Lesson' """

    name = models.CharField(max_length=100, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание урока")
    preview = models.ImageField(
        verbose_name="Картинка",
        upload_to="images/materials/lessons/photo/",
        default="images/materials/lessons/photo/default.png",
    )
    link_to_the_video = models.CharField(max_length=255, verbose_name="Ссылка на видео")
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        related_name="Уроки",
        verbose_name="Курс",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name
