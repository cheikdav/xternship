from django.conf.urls import url

from . import views

urlpatterns =[
    
    url(r'^$', views.index, name='index'),
    url(r'^(?P<prop_id>[0-9]+)/$', views.detail_prop, name = 'detail_prop')
]