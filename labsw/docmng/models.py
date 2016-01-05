from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import AbstractUser

class Userinfo(AbstractUser):
    number = models.CharField('学籍番号', max_length=8)
    FUCLTY_CHOICES = (
       ('システム工学群', 'システム工学群'),
       ('環境理工学群', '環境理工学群'),
       ('情報学群', '情報学群'),
       ('マネジメント学部', 'マネジメント学部'),
    )
    fuclty = models.CharField('学群', max_length=10, choices=FUCLTY_CHOICES)

class UserForm(ModelForm):
   class Meta:
      model = Userinfo
      fields = 'username', 'number', 'password', 'fuclty', 'email'
      widgets = {
        'password': forms.PasswordInput(),
      }    

class Document(models.Model):
    name = models.CharField(max_length=128)
    day = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=16)
    type = models.CharField(max_length=8)
    format = models.CharField(max_length=8)
    sid = models.CharField(max_length=8)
    path = models.FileField(upload_to='upload')
