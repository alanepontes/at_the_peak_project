# Std libs imports

# Core django imports

# Third party app imports
from rest_framework import serializers

# Local apps
from .models import Thumb


class ThumbSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thumb
        fields = ('id', 'is_positive', 'time', 'video')
