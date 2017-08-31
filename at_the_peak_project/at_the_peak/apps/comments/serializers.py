# Std libs imports

# Core django imports

# Third party app imports
from rest_framework import serializers

# Local apps
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'is_positive', 'time', 'video')
