from django.conf.urls import patterns, include, url
from tuitions import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tuitions.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.user_login, name='home'),
    url(r'^crm/',include('crm.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #userSearch
    url(r'^login/',views.user_login, name="login"),
    url(r'^logout/$','django.contrib.auth.views.logout',name='logout'),    



)
