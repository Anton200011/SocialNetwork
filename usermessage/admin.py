from django.contrib import admin
from .models import Message, Dialog, MessageText


# Register your models here.
# класс Inline позволяет включать модель в качестве подмодели в другую модель
class MessageInline(admin.TabularInline):
    model = Message
    raw_id_fields = ['dialog_id']


@admin.register(Dialog)
class DialogAdmin(admin.ModelAdmin):
    list_display = ['created', 'updated', 'participant1', 'participant2']
    list_filter = ['created', 'updated']
    inlines = [MessageInline]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'dialog_id', 'text', 'sender', 'recipient']
    list_filter = ['id', 'dialog_id', 'sender', 'recipient']


@admin.register(MessageText)
class MessageTextAdmin(admin.ModelAdmin):
    list_display = ['id', 'message_text']
