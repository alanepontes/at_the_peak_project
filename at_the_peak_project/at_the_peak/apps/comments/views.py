# Std libs imports

# Core django imports
from django.db import models

# Third party app imports
from rest_framework.response import Response
from rest_framework import viewsets, permissions

# Local apps
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    