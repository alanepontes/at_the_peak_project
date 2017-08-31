# Std libs imports

# Core django imports
from django.db import models

# Third party app imports
from rest_framework.response import Response
from rest_framework import viewsets, permissions

# Local apps
from .models import Thumb
from .serializers import ThumbSerializer


class ThumbViewSet(viewsets.ModelViewSet):
    queryset = Thumb.objects.all()
    serializer_class = ThumbSerializer
    permission_classes = (permissions.IsAuthenticated,)