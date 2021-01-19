from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from users.models import UserProfile


# def create_user_profile(created, instance, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#
# post_save.connect(create_user_profile, sender=User)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('This is signal')
    if created:
        UserProfile.objects.create(user=instance)
