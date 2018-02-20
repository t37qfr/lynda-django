from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.post_list, name='post_list'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$',views.post_list,name='post_list_by_tag'),
    url(r'^(?P<post>[-\w]+)$',views.post_detail,name='post_detail'),
]