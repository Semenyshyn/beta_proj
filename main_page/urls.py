from django.conf.urls import url
from . import views

app_name = 'main_page'
urlpatterns = [
    url(r'^$', views.stream_data, name='stream_data'),
    url(r'^list/$', views.message_list, name='message_list'),
]
