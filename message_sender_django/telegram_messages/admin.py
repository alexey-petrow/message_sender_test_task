from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'message', 'created_date']


admin.site.register(Message, MessageAdmin)
