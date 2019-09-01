from django.conf.urls import url
from . import views

app_name = 'care_point'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]