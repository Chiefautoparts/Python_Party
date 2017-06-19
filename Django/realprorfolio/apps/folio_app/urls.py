from django.conf.urls import url
from . import views 


urlpatterns = [
	url(r'^$', views.index),
	url(r'^projects$', views.show),
	url(r'^me$', views.about), 
	url(r'^testimonials$', views.quotes)
]