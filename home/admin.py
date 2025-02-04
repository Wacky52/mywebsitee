from django.contrib import admin

# Register your models here.
from home.models import  Setting
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Setting, SettingAdmin)
