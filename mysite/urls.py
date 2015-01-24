from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^mytime/$',mytime),
    url(r'^gettime/$',gettime),
    url(r'^time/(\d{1,2})/$',changetime),
    url(r'^bloglist/$',bloglist),
)
