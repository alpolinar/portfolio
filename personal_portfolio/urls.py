from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url



admin.site.site_header = 'Al Polinar Admin'
admin.site.site_title = 'Al Polin Admin'

from django_otp.admin import OTPAdminSite
admin.site.__class__ = OTPAdminSite

urlpatterns = [
    url(r'/', include('project_manager.urls')),
    path('backend/admin/', admin.site.urls),
]
