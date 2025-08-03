from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from venicle.models import CarsList, MotoList, Mileage
from venicle.serializers import CarSerializer, MotoSerializer, MileageSerializer, MotoMileageSerializer, \
    MotoCreateSerializer


class CarsViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = CarsList.objects.all()


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer


class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSerializer
    queryset = MotoList.objects.all()


class MotoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MotoSerializer
    queryset = MotoList.objects.all()


class MotoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MotoSerializer
    queryset = MotoList.objects.all()


class MotoDestroyAPIView(generics.DestroyAPIView):
    serializer_class = MotoSerializer
    queryset = MotoList.objects.all()


class MileageCreateAPIView(generics.CreateAPIView):
    serializer_class = MileageSerializer


class MotoMileageListAPIView(generics.ListAPIView):
    queryset = Mileage.objects.filter(moto__isnull=False)
    serializer_class = MotoMileageSerializer


class MileageListAPIView(generics.ListAPIView):
    serializer_class = MileageSerializer
    queryset = Mileage.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("car", "moto")
    ordering_fields = ("year", )
