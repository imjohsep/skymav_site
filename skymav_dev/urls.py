from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skymav.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('skymav.urls')),
    # url(r'^home/', include('home.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
