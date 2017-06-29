from django.conf.urls import url
from . import views

app_name='travel_app'
urlpatterns = [
    url(r'^$', views.index),	
    url(r'^travel$', views.travel)
]
