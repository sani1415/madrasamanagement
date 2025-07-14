from django.urls import path
from . import views, views_student_profile
from django.views.generic import TemplateView

urlpatterns = [
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('success/', views.attendance_success, name='attendance_success'),
    path('report/', views.attendance_report, name='attendance_report'),
    path('students/', views_student_profile.student_list, name='student_list'),
    path('student/<str:unique_id>/', views_student_profile.student_profile, name='student_profile'),
]
