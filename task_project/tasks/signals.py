
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, User


# Create a new group and assign a user
@receiver(post_save, sender=User)
def create_user_group(sender, instance, created, **kwargs):
    admin_group = Group.objects.create(name="Admin")
    user = User.objects.get(username="admin_user")
    user.groups.add(admin_group)