from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'friendlist'

urlpatterns = [
    url(r'^delete/(?P<user_id>[0-9]+)/(?P<owner_id>[0-9]+)$', views.delete_friend, name='delete_friend'),
    url(r'^add/(?P<user_id>[0-9]+)/(?P<owner_id>[0-9]+)$', views.add_friend, name='add_friend'),
    url(r'^list/(?P<owner_id>[0-9]+)', views.FriendView.as_view(), name="friend_list"),
]
