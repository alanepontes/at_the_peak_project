# Std libs imports

# Core django imports

# Third party app imports
from rest_framework import serializers


# Local apps
from .models import Video
from ..themes.models import Theme
from ..thumbs.serializers import ThumbSerializer


class VideoSerializer(serializers.ModelSerializer):
    themes = serializers.SlugRelatedField(many=True, queryset=Theme.objects.all(), slug_field='name')

    class Meta:
        model = Video
        fields = ('id', 'title', 'date_uploaded', 'views', 'themes', 'score')