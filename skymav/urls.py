from django.conf.urls import patterns, url

from skymav import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^name/', views.get_name, name='name'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^documentation/', views.documentation, name='documentation')
	# url(r'^mailgun/', views.mailgun, name='mailgun')
)