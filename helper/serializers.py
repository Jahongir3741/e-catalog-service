from rest_framework import serializers
from .models import Serial, Fond, Category, Genre, Region, Language, Mtv, Format


class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial
        fields = "__all__"
        extra_kwargs = {
            "created": {"read_only": True},
            "updated": {"read_only": True}

        }


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name']


class MtvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mtv
        fields = ['name']


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ['name']
