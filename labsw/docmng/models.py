from django.db import models
class Userinfo(models.Model):
    name = models.CharField(max_length=200)
    sid = models.DateTimeField('date published')
    passwd = models.CharField(max_length=8)
    faculty = models.CharField(max_length=8)
    email = models.EmailField()
    
class Document(models.Model):
    name = models.CharField(max_length=128)
    day = models.DateTimeField('date published')
    author = models.CharField(max_length=16)
    #def __unicode__(self):
    #   return self.author
    type = models.CharField(max_length=8)
    format = models.CharField(max_length=8)
    sid = models.CharField(max_length=8)
    path = models.FileField(upload_to=None)
    def __str__(self):
        return self.name

# Create your models here.
