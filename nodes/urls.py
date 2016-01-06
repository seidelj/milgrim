from django.conf.urls import url
from nodes import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^path/(?P<tree>[aA-zZ]*)/(?P<event>[0-9]*)/$', views.node, name="node"),
]
