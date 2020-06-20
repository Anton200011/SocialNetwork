from django.urls import path
from basic import views


urlpatterns = [
    path('', views.start_view),
]
