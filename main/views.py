from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import InformationSerializer, PosterSerializer, CadreSerializer
from .models import Information, Poster, Cadre
from rest_framework.parsers import MultiPartParser, FormParser


class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer

    @action(methods=["POST"], detail=True)
    def poster(self, request, *args, **kwargs):
        serializer = PosterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        obj = self.get_object()
        obj.poster_id = serializer.data.get("pk")
        obj.save()
        return Response(data={"msg": "Ok"}, status=status.HTTP_201_CREATED)

    @action(methods=["DELETE"], detail=True)
    def deletePoster(self, request, *args, **kwargs):
        obj = self.get_object()
        pk = obj.poster.pk
        print(pk)
        obj.poster.delete()
        poster = Poster.objects.get(pk=pk)
        print(poster)
        poster.delete()
        return Response(data={"msg": "Ok"}, status=status.HTTP_204_NO_CONTENT)


