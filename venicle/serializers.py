from rest_framework import serializers

from venicle.models import CarsList, MotoList, Mileage


class MileageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mileage
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    last_mileage = serializers.IntegerField(source="mileage_set.all.first.mileage")
    mileage = MileageSerializer(many=True)

    class Meta:
        model = CarsList
        fields = "__all__"


class MotoSerializer(serializers.ModelSerializer):
    last_mileage = serializers.SerializerMethodField()

    @staticmethod
    def get_last_mileage(instance):
        if instance.mileage.all().first():
            return instance.mileage.all().first().mileage
        return 0

    class Meta:
        model = MotoList
        fields = "__all__"


class MotoMileageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer()

    class Meta:
        model = Mileage
        fields = ("mileage", "year", "moto")


class MotoCreateSerializer(serializers.ModelSerializer):
    mileage = MileageSerializer(many=True)

    class Meta:
        model = MotoList
        fields = "__all__"

    def create(self, validated_data):
        mileage = validated_data.pop("mileage")

        moto_item = MotoList.objects.create(**validated_data)

        for obj in mileage:
            Mileage.objects.create(**obj, moto=moto_item)

        return moto_item