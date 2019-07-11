from django.conf.urls import url
from . import views

app_name='Demoapp'
urlpatterns = [

url(r'^$',views.base),
url(r'^home$',views.home),
url(r'^courses$',views.courses),
url(r'^ourgallery$',views.ourgallery),
url(r'^team$',views.team),
url(r'^contact$',views.contact),
url(r'^feedback$',views.feedback),
url(r'^register$',views.register),
url(r'^index$',views.index),
]
