from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^list/', views.UserView.as_view(), name="user_list"),
    url(r'^profile/(?P<user_id>[0-9]+)$', views.UserProfile.as_view(), name="user_profile"),
    url(r'^edit/(?P<pk>[0-9]+)$', views.UserEditProfile.as_view(), name="user_edit"),
    url(r'^delete/(?P<pk>[0-9]+)$', views.UserDeleteProfile.as_view(), name="user_delete"),
]
