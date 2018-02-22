from django.conf.urls import url
from . import views
#auth



urlpatterns = [
    url(r'^$',views.dashboard, name='dashboard'),
    #Login logout
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login', name='logout_than_login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^edit/$', views.edit, name='edit'),
    #reverse match error
    #url(r'^password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    #url(r'^password-change-done/$', 'django.contrib.auth.views.password_change_done',name='password_change_done'),
]