from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)      # we have a sender here (sender=User), and a signal 'post_save', SO:
                                       # when a User is saved, then send this signal - "post_save"
                                       # this signal is going to be received by this receiver (@receiver)
                                       # and this receiver is this "create_profile" function. And this function takes
                                       # all of these arguments (sender, instance, created, **kwargs) that
                                       # our 'post_save' signal passed to it (and one of those is
                                       # instance of the User, and one of those is "created": instance=User)
                                        # So if user was created => create the Profile object for that user.
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()