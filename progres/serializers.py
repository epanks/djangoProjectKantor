from rest_framework import serializers
from .models import *


class PaguPlainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagu
        fields = '__all__'


class PaketSerializer(serializers.ModelSerializer):
    pagu = PaguPlainSerializer(read_only=True, many=True)

    class Meta:
        model = Paket
        fields = '__all__'


class PaketPlainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paket
        fields = '__all__'


class PaguSerializer(serializers.ModelSerializer):
    paket = PaketPlainSerializer(many=False)

    class Meta:
        model = Pagu
        fields = '__all__'