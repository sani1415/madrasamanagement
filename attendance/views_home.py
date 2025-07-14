from django.http import HttpResponse

def home(request):
    return HttpResponse('<h2>Welcome to Madrasah Management System</h2><ul><li><a href="/admin/">Admin Panel</a></li><li><a href="/attendance/report/">Attendance Report</a></li></ul>')

