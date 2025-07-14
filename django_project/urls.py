from django.contrib import admin
from django.urls import path, include
from attendance.views_home import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('attendance/', include('attendance.urls')),
]

