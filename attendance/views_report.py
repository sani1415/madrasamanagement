
from .models import Attendance, Student
from django.db.models import Q

def attendance_report(request):
    class_filter = request.GET.get("class", "")
    date_filter = request.GET.get("date", "")
    
    records = Attendance.objects.select_related("student").all()

    if class_filter:
        records = records.filter(student__class_name=class_filter)
    if date_filter:
        records = records.filter(date=date_filter)
        
    classes = Student.objects.values_list("class_name", flat=True).distinct()
    
    return render(request, "attendance/report.html", {
        "records": records,
        "classes": classes,
        "selected_class": class_filter,
        "selected_date": date_filter,
    })

