from django.urls import path, re_path
from .views import (
    CraneDetail,
    HDVDashboardView,
    sample_page,
    error_page
)
from django.conf import settings  
from django.conf.urls.static import static  


urlpatterns = [
    # path("", HDVHome.as_view(), name="home"),
    path("", HDVDashboardView.as_view(), name="dashboard_view"),
    # path("crane/detail/", CraneDetail.as_view(), name="equip_single"),
    path('crane/<int:pk>', CraneDetail.as_view(), name='crane_detail'),
    path('home', sample_page, name='name'),
    re_path('.*/', error_page, name='error'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)