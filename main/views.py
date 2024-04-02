from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import InformationSerializer, PosterSerializer, CadreSerializer
from .models import Information, Poster, Cadre
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend


class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['region', 'language', 'year']
    search_fields = ['name', 'brief_data', 'summary', 'mtv_index', 'location_on_server']
    filterset_fields = ['category__name', 'genre__name', 'region__name', 'year']

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
        obj.poster.delete()
        poster = Poster.objects.get(pk=pk)
        poster.delete()
        return Response(data={"msg": "Ok"}, status=status.HTTP_204_NO_CONTENT)


class CadreViewSet(viewsets.ModelViewSet):
    queryset = Cadre.objects.all()
    serializer_class = CadreSerializer
