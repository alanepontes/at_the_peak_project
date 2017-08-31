# Std libs imports
from datetime import datetime, timedelta, timezone

# Core django imports
from django.db import models
from django.db.models import F

# Third party app imports

# Local apps
from .utils import Util

class VideoManager(models.Manager):
    
    def recents(self):
        return super(VideoManager, self).get_queryset().filter(date_uploaded__range=[datetime.now(timezone.utc) - timedelta(Util.DAYS_IN_YEAR), datetime.now(timezone.utc)])