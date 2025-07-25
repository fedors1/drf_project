from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from django.urls import path

from materials.views import LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, LessonRetrieveAPIView, \
    LessonDestroyAPIView, CourseViewSet

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")


urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lesson-list"),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson-update"),
    path("lesson/detail/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson-detail"),
    path("lesson/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson-delete"),
] + router.urls
