#rango
from django.conf.urls import url
from FinishOnTime import views
from django.conf.urls import include

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index', views.index, name='index'),
	url(r'^library', views.library, name='library'),
	url(r'^project', views.project, name='project'),
	url(r'^add', views.add, name='add'),
	url(r'^edit', views.edit, name='edit'),
	url(r'^about', views.about, name='about'),
	url(r'^', include('registration.backends.simple.urls')),
]
