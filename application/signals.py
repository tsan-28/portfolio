from django.dispatch import receiver
from .models import Profile
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.contrib.auth.models import User


@receiver(pre_save, sender=Profile) 
def pre_save_receiver(sender, instance, *args, **kwargs): 
    if not instance.slug: 
        instance.slug = unique_slug_generator(instance) 

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()