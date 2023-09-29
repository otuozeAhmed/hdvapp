from django.contrib import admin
from django.urls import path, include
from django.conf import settings  
from django.conf.urls.static import static



admin.site.site_header = 'HDE Admin Page'
#Add the below line
admin.site.index_title = 'Admin Apps'

urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path("", include("dashboard.urls")),
] 


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)