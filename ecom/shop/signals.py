from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
       user = instance
       profile = Profile.objects.create(
           user = user,
           username = user.username,
           email = user.email,
           name = user.first_name,
        )
       subject = 'Welcome to our shop'
       message = 'We are glad to you are here'
       print(subject)
       send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )

@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

# post_save.connect(createProfile, sender=User)
# post_delete.connect(deleteUser, sender=Profile)