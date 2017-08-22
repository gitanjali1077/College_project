"""UnistashFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from Functions.views import index,file1 ,company,index1,logout
from django.conf.urls import include ,url
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^logout/$',logout ,   name='logout'),

    url(r'^(?P<string>[\w\-]+)/$',index,name='index'),
     url(r'^login/(?P<string>[\w\-]+)/$',index,name='index'),
   
    url(r'^notes/(?P<string>[\w\-]+)/$',file1, name='files'),
    url(r'^interview/(?P<company>[\w\-]+)/$', company ,name='company'),
    #url(r'^content/(?P<string>[\w\-]+)/(?P<stri>[\w\-]+)/$',sidebar, name='side'),
   url(r'^captcha/', include('captcha.urls')),
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

