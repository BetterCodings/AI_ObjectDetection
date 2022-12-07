from django.contrib import admin
from django.urls import path
from rest_framework import routers
from account import views as account_views
from submit import views as submit_views

from django.urls import include, re_path
from django.conf.urls.static import static
from django.conf import settings

# router0 = routers.DefaultRouter()
# router0.register(r'accounts', account_views.AccountViewset)
# router1 = routers.DefaultRouter()
# router1.register(r'lectures', submit_views.LectureViewset)
# router2 = routers.DefaultRouter()
# router2.register(r'classes', submit_views.ClassViewset)
# router3 = routers.DefaultRouter()
# router3.register(r'attendences', submit_views.AttendenceViewset)
# router4 = routers.DefaultRouter()
# router4.register(r'students', submit_views.StudentViewset)
router = routers.DefaultRouter()
router.register(r'posts', submit_views.PostsViewset)
urlpatterns = [
    path('login/', account_views.login),

    path("lecture/<ID>/",submit_views.lecture),
    path("class/today/<pID>/",submit_views.today_class),
    path("class/<pID>/",submit_views.class_),
    
    path("student/<ID>/",submit_views.lecture_student),
    
    path("attendence/update/",submit_views.update_attendence),
    path("attendence/",submit_views.select_attendence),

    path("attendence/student/",submit_views.student),

    re_path(r'^',include(router.urls)),
    # re_path(r'^',include(router0.urls)),
    # re_path(r'^',include(router1.urls)),
    # re_path(r'^',include(router2.urls)),
    # re_path(r'^',include(router3.urls)),
    # re_path(r'^',include(router4.urls)),
    path("admin/", admin.site.urls),
    path('auth', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
