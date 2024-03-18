from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InformationViewSet


router = DefaultRouter()
router.register("information", InformationViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
