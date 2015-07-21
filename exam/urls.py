from django.conf.urls import patterns, url
from exam import views

urlpatterns = patterns('',
	url(r'^$', views.Index, name='home'),
	url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
	url(r'^survey/(?P<id>\d+)/$', views.SurveyDetail, name='survey_detail'),
	url(r'^confirm/(?P<uuid>\w+)/$', views.Confirm, name='confirmation'),
)


