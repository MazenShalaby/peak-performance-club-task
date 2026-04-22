from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Member

# create your signals here


@receiver(post_save, sender=Member)
def on_postsave_print(sender, instance, created, **kwargs):
    if created:
        print(f"Printing created instance with name: {instance.name}")
    else:
        print(f"Printing updated instance with name: {instance.name}")