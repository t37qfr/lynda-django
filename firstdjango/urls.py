from django.conf.urls import include, url
from django.contrib import admin

from inventory import views
'''Media'''
from django.conf import settings
from django.conf.urls.static import static


'''ACCOUNT
Bug? I could not put these lines to account/urls : noReverseMatch error. A namespace issue.
Django cannot find it under account: namespace
'''


urlpatterns  = [
    url(r'^shop/', include('shop.urls', namespace='shop')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^blog/',include('blog.urls',namespace='blog',app_name='blog')),
    url(r'^images/',include('images.urls',namespace='images',app_name='images')),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    # ACCOUNT
    url(r'^account/', include('account.urls', namespace='account', app_name='account')),
    url(r'^admin/', include(admin.site.urls)),
    #social auth
    url(r'^social-auth/',include('social.apps.django_app.urls',namespace='social')),
]

'''
MEDIA
in production: same server host media files -> Slow server (application server vs. 'hosting server')
'''
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

