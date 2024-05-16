from rest_framework import viewsets
from .serializers import SerialSerializer, RegionSerializer, LanguageSerializer, MtvSerializer, FormatSerializer
from .models import Serial, Region, Language, Mtv, Format
from rest_framework.permissions import IsAuthenticated


class SerialViewSet(viewsets.ModelViewSet):
    queryset = Serial.objects.all()
    serializer_class = SerialSerializer
    permission_classes = [IsAuthenticated]


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [IsAuthenticated]


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]


class MtvViewSet(viewsets.ModelViewSet):
    queryset = Mtv.objects.all()
    serializer_class = MtvSerializer
    permission_classes = [IsAuthenticated]


class FormatViewSet(viewsets.ModelViewSet):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer
    permission_classes = [IsAuthenticated]

