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
