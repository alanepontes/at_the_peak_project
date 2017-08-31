# Std libs imports
from datetime import datetime, timezone

# Core django imports
from django.db import models
from django.db.models import When, Case, Sum, IntegerField

# Third party app imports

# Local apps
from .managers import VideoManager
from .utils import Util
from ..themes.models import Theme


class Video(models.Model):
    
    title = models.CharField(max_length=100)
    date_uploaded = models.DateTimeField()
    views = models.PositiveIntegerField()
    themes = models.ManyToManyField(Theme, related_name='videos')

    objects = VideoManager()    

    @property
    def score(self):
        return self.views * self.time_factor * self.positivity_factor

    @property
    def time_factor(self):
        diff_beetween_datas = datetime.now(timezone.utc) - self.date_uploaded
        
        return max(0, 1 - (diff_beetween_datas.days/Util.DAYS_IN_YEAR))

    @property
    def positivity_factor(self):
        importance_to_comment = 0.7
        importance_to_thumbs = 0.3
        return (importance_to_comment * self.good_comments) + (importance_to_thumbs * self.thumbs_up)

    @property
    def thumbs_up(self):
        if self.thumbs.exists() is False: return 0 
        else: 
            thumbs_up, thumbs_down = self.total_thumbs_up, self.total_thumbs_down
            return thumbs_up/(thumbs_up + thumbs_down)


    @property
    def good_comments(self):
        if self.comments.exists() is False: return 0 
        else: 
            good_comments, negative_comments = self.total_good_comments, self.total_negative_comments
            return good_comments/(good_comments + negative_comments)

    
    @property
    def total_thumbs_up(self):
        if self.thumbs.exists() is False: return 0 
        else:
            return self.thumbs.values('is_positive').aggregate(
            thumbs_up = Sum(
                            Case(
                                When(is_positive=True, then=1),
                                output_field=IntegerField(),
                            )
                        ))['thumbs_up']
    @property
    def total_thumbs_down(self):
        if self.thumbs.exists() is False: return 0 
        else: 
            return self.thumbs.values('is_positive').aggregate(
                        thumbs_down = Sum(
                            Case(
                                When(is_positive=False, then=1),
                                output_field=IntegerField(),
                            )
                        ))['thumbs_down']
    @property
    def total_good_comments(self):
        if self.comments.exists() is False: return 0 
        else: 
            return self.comments.values('is_positive').aggregate(
                       comments_up = Sum(
                            Case(
                                When(is_positive=True, then=1),
                                output_field=IntegerField(),
                            )
                        ))['comments_up']

    @property
    def total_negative_comments(self):
        if self.comments.exists() is False: return 0 
        else: 
            return self.comments.values('is_positive').aggregate(
                        comments_down = Sum(
                            Case(
                                When(is_positive=False, then=1),
                                output_field=IntegerField(),
                            )
                        ))['comments_down']
   

    def __str__(self):
        return self.title