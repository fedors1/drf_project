from django.urls import path
from rest_framework.routers import DefaultRouter

from venicle.apps import VenicleConfig
from venicle.views import (
    CarsViewSet,
    MotoCreateAPIView,
    MotoDestroyAPIView,
    MotoListAPIView,
    MotoRetrieveAPIView,
    MotoUpdateAPIView, MileageCreateAPIView, MotoMileageListAPIView, MileageListAPIView,
)

app_name = VenicleConfig.name


router = DefaultRouter()
router.register(r"cars", CarsViewSet, basename="cars")


urlpatterns = [
    path("moto/create/", MotoCreateAPIView.as_view(), name="moto-create"),
    path("moto/", MotoListAPIView.as_view(), name="moto-list"),
    path("moto/<int:pk>/", MotoRetrieveAPIView.as_view(), name="moto-get"),
    path("moto/update/<int:pk>/", MotoUpdateAPIView.as_view(), name="moto-update"),
    path("moto/delete/<int:pk>/", MotoDestroyAPIView.as_view(), name="moto-destroy"),

    #mileage
    path("mileage/", MileageListAPIView.as_view(), name="mileage-list"),
    path("mileage/create/", MileageCreateAPIView.as_view(), name="mileage-create"),
    path("moto/mileage/", MotoMileageListAPIView.as_view(), name="moto-mileage-create"),
] + router.urls
