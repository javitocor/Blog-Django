from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from .models import *

def create_blogger(sender, instance, created, **kwargs):
	if created:
		Blogger.objects.create(
			user=instance,
			first_name=instance.first_name,
			last_name=instance.last_name,
			email=instance.email,
			)
		print("Blogger Created!")


def update_blogger(sender, instance, created, **kwargs):
	if created == False:
		instance.blogger.first_name = instance.first_name
		instance.blogger.last_name = instance.last_name
		instance.blogger.email = instance.email
		instance.blogger.save()
		print("Blogger updated!")

post_save.connect(create_blogger, sender=User)
post_save.connect(update_blogger, sender=User)

