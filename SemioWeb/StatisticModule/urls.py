from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.z_list, name='z_list'),
]