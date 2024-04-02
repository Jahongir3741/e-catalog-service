from rest_framework import viewsets
from .serializers import SerialSerializer, RegionSerializer, LanguageSerializer, MtvSerializer, FormatSerializer
from .models import Serial, Region, Language, Mtv, Format


class SerialViewSet(viewsets.ModelViewSet):
    queryset = Serial.objects.all()
    serializer_class = SerialSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class MtvViewSet(viewsets.ModelViewSet):
    queryset = Mtv.objects.all()
    serializer_class = MtvSerializer


class FormatViewSet(viewsets.ModelViewSet):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer
