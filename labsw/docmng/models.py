from django.db import models
from django.forms import ModelForm
from django import forms

class Userinfo(models.Model):
    username = models.CharField(max_length=16)
    number = models.IntegerField()
    password = models.CharField(max_length=8)
    FUCLTY_CHOICES = (
       ('システム工学群', 'システム工学群'),
       ('環境理工学群', '環境理工学群'),
       ('情報学群', '情報学群'),
       ('マネジメント学部', 'マネジメント学部'),
    )
    fuclty = models.CharField(max_length=10, choices=FUCLTY_CHOICES)
    email = models.EmailField()
    def __str__(self):
      return self.username

class UserForm(ModelForm):
   class Meta:
      model = Userinfo
      fields = '__all__'
      widgets = {
        'password': forms.PasswordInput(),
      }    

class Document(models.Model):
    name = models.CharField(max_length=128)
    day = models.DateTimeField('date published')
    author = models.CharField(max_length=16)
    type = models.CharField(max_length=8)
    format = models.CharField(max_length=8)
    sid = models.CharField(max_length=8)
    path = models.FileField(upload_to=None)
