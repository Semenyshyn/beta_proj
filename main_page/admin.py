from django.contrib import admin
from .models import Messages


class MessagesAdmin(admin.ModelAdmin):
    list_display = ['method', 'body', 'encoding', 'content_type']


admin.site.register(Messages, MessagesAdmin)
