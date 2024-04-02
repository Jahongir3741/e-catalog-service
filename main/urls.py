from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InformationViewSet, CadreViewSet


router = DefaultRouter()
router.register("information", InformationViewSet)
router.register("cedre", CadreViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
