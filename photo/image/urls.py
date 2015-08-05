from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',
	# ex: /
	url(r'^$', views.ImageAddView.as_view(), name='home'),

	# ex: /images/4
	url(r'^images/(?P<pk>[0-9]+)/$', views.ImageFavView.as_view(), name='imageDetail'),

	# ex: /images/4/fav
	#url(r'^images/(?P<pk>[0-9]+)/fav/$', views.ImageFavView.as_view(), name='favorite'),

	# ex: /favorites/1
)