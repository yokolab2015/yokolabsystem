from django.contrib import admin
from .models import Message

class ChoiceInline(admin.StackedInline):
    model = Message
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['message']}),
        ('Date information', {'fields': ['title'],'classes':['collapse']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Message)

# Register your models here.