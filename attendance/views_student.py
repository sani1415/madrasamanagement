
from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all().order_by('roll_number')
    return render(request, 'attendance/student_list.html', {'students': students})

