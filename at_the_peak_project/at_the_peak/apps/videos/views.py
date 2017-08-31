# Std libs imports

# Core django imports
from django.db import models

# Third party app imports
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework import viewsets, permissions

# Local apps
from .models import Video
from .serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @list_route()
    def recents(self, request):
        serializer = self.get_serializer(Video.objects.recents(), many=True)
        return Response(serializer.data)