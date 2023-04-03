from django.contrib.auth.models import User
from django.db import models

class Photo(models.Model):
    author = models.ForeignKey(
                                User,
                                on_delete = models.CASCADE,
                            )
    title = models.CharField(max_length=80, blank=False, null=False)
    image = models.ImageField(upload_to='media/images/',blank=False )
    description = models.TextField(max_length=255, blank=True, null=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[0:80]