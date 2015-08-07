from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',
	# ex: /
	url(r'^$', views.ImageAddView.as_view(), name='home'),

	# ex: /images/
	url(r'^images/$', views.ImageListView.as_view(), name='imageList'),

	# ex: /images/4
	url(r'^images/(?P<pk>[0-9]+)/$', views.ImageDetailView.as_view(), name='imageDetail'),

	# ex: /favList/
	url(r'^favList/$', views.FavList.as_view(), name='favoriteList'),
)