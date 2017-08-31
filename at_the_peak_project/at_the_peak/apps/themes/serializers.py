# Std libs imports

# Core django imports

# Third party app imports
from rest_framework import serializers

# Local apps
from .models import Theme


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'name', 'pontuation_in_all_videos', 'pontuation_in_recents_videos')
        read_only_fields = ('pontuation_in_all_videos', 'pontuation_in_recents_videos')