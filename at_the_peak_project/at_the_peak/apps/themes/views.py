# Std libs imports

# Core django imports
from django.db import models

# Third party app imports
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework import viewsets, permissions

# Local apps
from .models import Theme
from .serializers import ThemeSerializer


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @list_route()
    def populars(self, request):
        serializer = self.get_serializer(Theme.objects.all().order_by('-pontuation_in_all_videos'), many=True)
        return Response(serializer.data)

