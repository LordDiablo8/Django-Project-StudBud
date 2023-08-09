from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.sessions.models import Session

@receiver(user_logged_in)
def update_user_last_activity(sender, request, user,**kwargs):
    now = timezone.now()
    user.last_activity = now
    user.save()

@receiver(user_logged_out)
def clear_user_last_activity(sender, request, user, **kwargs):
    user.last_activity = None
    user.save()
    