__author__ = 'Pavan Kotehal'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListResponse.as_view(), name='response_list'),
    url(r'^users/$', views.ListUsers.as_view(), name='users_list'),
    url(r'^(?P<survey_pk>\d+)/survey/$',
        views.ListCreateResponse.as_view(),
        name='response_list'),

]