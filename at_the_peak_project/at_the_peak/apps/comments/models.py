# Std libs imports

# Core django imports
from django.db import models

# Third party app imports

# Local apps
from ..videos.models import Video


class Comment(models.Model):
    is_positive = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.is_positive)