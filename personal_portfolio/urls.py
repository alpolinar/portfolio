from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from django.conf.urls import (handler404, handler500)

admin.site.site_header = 'Al Polinar Admin'
admin.site.site_title = 'Al Polin Admin'

from django_otp.admin import OTPAdminSite
admin.site.__class__ = OTPAdminSite

urlpatterns = [
    url(r'^django-backend/admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^$', include('project_manager.urls'), name='home_page'),
]

handler404 = 'project_manager.views.handler404'
handler500 = 'project_manager.views.handler500'