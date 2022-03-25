"""tution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from base_app import views



urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.login, name='login'),
    re_path(r'^Student_logout$', views.Student_logout, name='Student_logout'),
    re_path(r'^Admin_logout$', views.Admin_logout, name='Admin_logout'),
    re_path(r'^Student_index$', views.Student_index, name='Student_index'),
    re_path(r'^Student_applyleave_cards/$', views.Student_applyleave_cards, name='Student_applyleave_cards'),
    re_path(r'^Student_leavereq/$', views.Student_leavereq, name='Student_leavereq'),
    re_path(r'^Student_reqedleave/$', views.Student_reqedleave, name='Student_reqedleave'),
    re_path(r'^Student_progressreport/$', views.Student_progressreport, name='Student_progressreport'),




    re_path(r'^Admin_index$', views.Admin_index, name='Admin_index'),
    re_path(r'^Admin_dashboard$', views.Admin_dashboard, name='Admin_dashboard'),
    re_path(r'^logout$', views.logout, name='logout'),


    re_path(r'^Man_index$', views.Man_index, name='Man_index'),
    re_path(r'^MAN_Report$', views.MAN_Report, name='MAN_Report'),
    # re_path(r'^MAN_Reportedissue$', views.MAN_Reportedissue, name='MAN_Reportedissue'),
    re_path(r'^MAN_ReportedissueShow/(?P<id>\d+)$', views.MAN_ReportedissueShow, name='MAN_ReportedissueShow'),
    re_path(r'^MAN_rep/(?P<id>\d+)/$', views.MAN_rep, name='MAN_rep'),
    re_path(r'^MAN_ReportedissueShow1/(?P<id>\d+)/$',views.MAN_ReportedissueShow1, name='MAN_ReportedissueShow1'),
    re_path(r'^MAN_manager_report$', views.MAN_manager_report, name='MAN_manager_report'),
    re_path(r'^MAN_Reportissue$', views.MAN_Reportissue, name='MAN_Reportissue'),
    re_path(r'^MAN_reportsuccess$', views.MAN_reportsuccess, name='MAN_reportsuccess'),
    re_path(r'^MAN_manger_reportedissues$', views.MAN_manger_reportedissues, name='MAN_manger_reportedissues'),
    re_path(r'^MAN_manger_reportedissues1/(?P<id>\d+)/$', views.MAN_manger_reportedissues1, name='MAN_manger_reportedissues1'),

    re_path(r'^change_password$', views.change_password, name='change_password'),


    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
