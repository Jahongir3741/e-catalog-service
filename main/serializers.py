from rest_framework import serializers
from .models import Information, Poster, Cadre


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ['pk', 'image']


class CadreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadre
        fields = '__all__'
