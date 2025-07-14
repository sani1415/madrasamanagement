from django.shortcuts import render, get_object_or_404
from .models import Student, Attendance

def student_profile(request, unique_id):
    student = get_object_or_404(Student, unique_id=unique_id)
    attendance_records = Attendance.objects.filter(student=student).order_by('-date')

    total_days = attendance_records.count()
    days_present = attendance_records.filter(present=True).count()
    attendance_percentage = (days_present / total_days) * 100 if total_days > 0 else 0

    return render(request, 'attendance/student_profile.html', {
        'student': student,
        'attendance_records': attendance_records,
        'total_days': total_days,
        'days_present': days_present,
        'attendance_percentage': round(attendance_percentage, 2)
    })

def student_list(request):
    students = Student.objects.all().order_by('class_name', 'roll_number')
    return render(request, 'attendance/student_list.html', {
        'students': students
    })
