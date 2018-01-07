
from django.db import models
from django.utils import timezone
from django.conf import settings 

class Board(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)

    def publish(self):
    	self.save()

    def __str__(self):
        return self.name  

