# Std libs imports
from functools import reduce

# Core django imports
from django.db import models

# Third party app imports

# Local apps


class Theme(models.Model):
    name = models.CharField(max_length=60, unique=True)
    pontuation_in_all_videos = models.DecimalField(max_digits=20, decimal_places=12, null=True, blank=True)
    pontuation_in_recents_videos = models.DecimalField(max_digits=20, decimal_places=12, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.pontuation_in_all_videos = self.__pontuation_in_all_videos()
        self.pontuation_in_recents_videos = self.__pontuation_in_recents_videos()
        return super(Theme, self).save(*args, **kwargs)

    def __pontuation_in_all_videos(self):
        if self.videos.exists() is False: return 0 
        else:
            return reduce(lambda acc, obj: acc + obj.score, self.videos.all(), 0)

    def __pontuation_in_recents_videos(self):
        if self.videos.recents().exists() is False: return 0 
        else:
            return reduce(lambda acc, obj: acc + obj.score, self.videos.recents(), 0)

    def __str__(self):
        return "{} {}".format(self.id, self.name)