from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrackViewSet

router = DefaultRouter()
router.register('track', TrackViewSet)

urlpatterns = [
  path('', include(router.urls))
]