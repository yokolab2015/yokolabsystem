from django.contrib import admin
from accounts.models import Userinfo

class UserAdmin(admin.ModelAdmin):
   list_display = ('number', 'username',)
   list_display_links = ('username',)
admin.site.register(Userinfo, UserAdmin)
