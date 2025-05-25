from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile, Post  
from .tasks import send_post_notification  
User = get_user_model()

# Create profile when user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save profile when user is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

#  Send post notification when a post is created
@receiver(post_save, sender=Post)
def notify_on_post_creation(sender, instance, created, **kwargs):
    if created:
        send_post_notification.delay(instance.id)
