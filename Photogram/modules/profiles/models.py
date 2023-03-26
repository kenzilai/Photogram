from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(
                                User,
                                on_delete=models.CASCADE,
                                related_name='profile'
                            )
    image = models.ImageField(upload_to='media/avatars/', default='/media/avatars/default_profile.png')
    headline = models.CharField(max_length=60, blank=True, null=False)
    city = models.CharField(max_length=60, blank=True, null=False)
    country = models.CharField(max_length=20, blank=True, null=False)

    def __str__(self):
        return self.user.username[0:30]
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a new profile when a User is created."""
    if created:
            Profile.objects.create(user=instance)