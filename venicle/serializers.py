from rest_framework import serializers

from venicle.models import CarsList, MotoList


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarsList
        fields = "__all__"


class MotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = MotoList
        fields = "__all__"
