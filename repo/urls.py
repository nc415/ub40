from django.conf.urls import include, url
from . import views
from repo.views import company_profile

urlpatterns =[
        url(r'^$', views.home, name="home"),
        url(r'^(?P<Company_Name>[\w\-]+)/$', views.company_profile, name='company_profile'),
        url(r'^(?P<Company_Name>[\w\-]+)/(?P<BU_Name>[\w\-]+)/$', views.BU_Profile, name='BU_Profile'),
]


