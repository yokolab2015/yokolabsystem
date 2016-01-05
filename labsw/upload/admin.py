from django.contrib import admin
from .models import Message

class ChoiceInline(admin.StackedInline):
    model = Message
    extra = 3


admin.site.register(Message)

# Register your models here.
