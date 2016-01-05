from django.db import models
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks', null = True)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=64)
    file = models.FileField(upload_to='upload')

@receiver(post_delete, sender=Message)
def delete_file(sender, instance, **kwargs):
    instance.file.delete(False)



    def __unicode__(self):
        return self.message

    def __unicode__(self):
        return self.title