from django.shortcuts import render, redirect
from .models import Student, Attendance
from .forms import AttendanceForm
from datetime import date

def mark_attendance(request):
    today = date.today()

    # Get attendance stats for today (if exists)
    today_records = Attendance.objects.filter(date=today)
    total_students = Student.objects.count()
    present_count = today_records.filter(present=True).count()
    absent_count = today_records.filter(present=False).count()

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            # Prevent duplicate marking for same date
            Attendance.objects.filter(date=today).delete()
            for student in Student.objects.all():
                present = form.cleaned_data.get(f'student_{student.id}', False)
                Attendance.objects.create(student=student, date=today, present=present)
            return redirect('attendance_success')
    else:
        form = AttendanceForm()

    return render(request, 'attendance/mark_attendance.html', {
        'form': form,
        'today': today,
        'total_students': total_students,
        'present_count': present_count,
        'absent_count': absent_count
    })

def attendance_success(request):
    return render(request, 'attendance/attendance_success.html')

def attendance_report(request):
    records = Attendance.objects.select_related('student').order_by('-date')
    class_filter = request.GET.get('class')
    date_filter = request.GET.get('date')
    if class_filter:
        records = records.filter(student__class_name=class_filter)
    if date_filter:
        records = records.filter(date=date_filter)
    classes = Student.objects.values_list('class_name', flat=True).distinct()
    return render(request, 'attendance/report.html', {
        'records': records,
        'classes': classes,
        'selected_class': class_filter,
        'selected_date': date_filter
    })
