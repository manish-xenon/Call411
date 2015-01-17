from django.conf.urls import url
from phones import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    url(r'^addphone/$', views.addPhone, name='addphone'),

    url(r'^search/$', views.search, name='search'),
    url(r'^suggest/$', views.suggest, name='suggest'),
    url(r'^(?P<model_number>[\w \-&+()]+)/$', views.detail, name='detail'),
    
    url(r'^(?P<model_number>[\w \-&+()]+)/edit/$', views.updatePhone, name='editphone'),
    url(r'^(?P<model_number>[\w \-&+()]+)/del/$', views.deletePhone, name='deletephone'),


    url(r'^api/v1/allPhones', views.allPhones, name='allPhones'),
    url(r'^api/v1/getPhone', views.getPhone, name='getPhone'),
    url(r'^api/v1/similarPhones', views.apiSuggest, name='apiSuggest'),
]
