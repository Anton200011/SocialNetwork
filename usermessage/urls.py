from django.urls import path
from . import views
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

app_name = 'message'

urlpatterns = [
    url(r'^message_del/(?P<mess_id>[0-9]+)/(?P<part1>[0-9]+)/(?P<part2>[0-9]+)$', views.remove_message,
        name='message_delete'),
    url(r'^delete_message/(?P<message_id>[0-9]+)$', csrf_exempt(views.remove_message)),
    url(r'^edit/(?P<message_id>[0-9]+)$', csrf_exempt(views.remove_message)),
    url(r'^send/(?P<sen_id>[0-9]+)/(?P<rec_id>[0-9]+)$', views.send_message, name='send_message'),
    url(r'^list/(?P<part1>[0-9]+)/(?P<part2>[0-9]+)$', views.message_list, name="message_list"),
    url(r'^dialogs/(?P<owner_id>[0-9]+)$', views.dialog_list, name="dialogs"),
    url(r'^dialog_del/(?P<sen_id>[0-9]+)/(?P<rec_id>[0-9]+)$', views.remove_dialog, name="dialog_delete"),

]
