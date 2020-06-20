from .models import Friend, FriendList
from django.contrib import admin


# Register your models here.
# класс Inline позволяет включать модель в качестве подмодели в другую модель
class MessageInline(admin.TabularInline):
    model = Friend
    raw_id_fields = ['f_list_id']


@admin.register(FriendList)
class FriendListAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner']
    list_filter = ['id', 'owner']
    inlines = [MessageInline]


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ['f_list_id', 'friend_id']
    list_filter = ['f_list_id', 'friend_id']
