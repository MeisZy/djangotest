from django.db import models

__all__ = ["Tasks"]

class Tasks(models.Model):

    """Model for each tasks"""

    title = models.CharField(max_length=255,null=True,blank= True)
    description=models.TextField(max_length=1000, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title