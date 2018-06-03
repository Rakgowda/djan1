from django.conf.urls import url
from . import views

app_name = 'sell'

urlpatterns = [
    url(r'^$', views.Home.as_view(),name='home'),
    url(r'^sell/add/$',views.AddItem.as_view(),name='additem'),
    url(r'^sell/update/(?P<pk>[0-9]+)$',views.UppItem.as_view(),name='uppitem'),
    url(r'^(?P<item>\w+)/$',views.IdView.as_view(),name ='sellid'),
    url(r'^api$',views.SellApi.as_view(),name = 'sellapi'),

]
