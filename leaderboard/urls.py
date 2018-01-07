from django.conf.urls import url
from . import views

urlpatterns=[url(r'^$',views.front_page,name='front_page'),
			 url(r'^board/(?P<pk>\d+)/$',views.link_page,name='link_page'),
			 url(r'^board/new/$',views.form_page,name='form_page'),
			 url(r'^form/(?P<pk>\d+)/edit/$', views.form_edit, name='form_edit'),
			 url(r'^board/(?P<pk>\d+)/delete/$', views.del_page, name='del_page'),
			 url(r'^form/signup/$',views.form_signup, name='form_signup'),
			 url(r'^form/signin/$',views.form_signin, name='form_signin'),
			 url(r'^form/signout/$',views.form_signout, name='form_signout')
			]