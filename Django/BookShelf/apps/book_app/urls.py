from django.conf.urls import url
from . import views

urlpatterns = [
	urls(r'^$', views.index)
	url(r'^new_book$', views.create)
]