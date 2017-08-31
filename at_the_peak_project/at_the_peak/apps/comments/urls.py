# Std libs imports

# Core django imports
from django.conf.urls import url, include

# Third party app imports
from rest_framework.routers import DefaultRouter

# Local apps
from .views import CommentViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'comments', CommentViewSet, 'comments')

urlpatterns = [
    url(r'^', include(router.urls)),
]