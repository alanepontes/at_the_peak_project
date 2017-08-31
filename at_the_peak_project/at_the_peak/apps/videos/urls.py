# Std libs imports

# Core django imports
from django.conf.urls import url, include

# Third party app imports
from rest_framework.routers import DefaultRouter

# Local apps
from .views import VideoViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'videos', VideoViewSet, 'videos')

urlpatterns = [
    url(r'^', include(router.urls)),
]