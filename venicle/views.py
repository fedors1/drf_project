from rest_framework import generics, viewsets

from venicle.models import CarsList, MotoList
from venicle.serializers import CarSerializer, MotoSerializer


class CarsViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = CarsList.objects.all()


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoSerializer


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
