from django.conf.urls import include, url
from django.contrib import admin

from inventory import views

urlpatterns  = [
    url(r'^$',views.index,name='index'),
    url(r'^blog/',include('blog.urls',namespace='blog',app_name='blog')),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^account/', include('account.urls', namespace='account', app_name='account')),
    url(r'^admin/', include(admin.site.urls)),
]
