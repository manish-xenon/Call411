from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    # route to phones module
    url(r'^', include('phones.urls', namespace="phones")),
)
