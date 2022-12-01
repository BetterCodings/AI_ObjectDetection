
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from bg_removal import views
from django.urls import include, re_path

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewset)

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^',include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]