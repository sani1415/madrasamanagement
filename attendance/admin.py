from django.contrib import admin
from .models import Student
from .classroom import ClassRoom

admin.site.register(Student)
admin.site.register(ClassRoom)

