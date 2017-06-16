from django.conf.urls import url
from . import views

app_name = 'things_app'
urlpatterns = [
		url(r'^$', views.index)
	]