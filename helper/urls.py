from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('serial', views.SerialViewSet)
router.register('region', views.RegionViewSet)
router.register('language', views.LanguageViewSet)
router.register('mtv', views.MtvViewSet)
router.register('format', views.FormatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
