from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    roll_number = models.IntegerField()
    unique_id = models.CharField(max_length=10, unique=True)
    mobile = models.CharField(max_length=20)
    address = models.TextField()
    sub_district = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('left', 'Left'),
        ('transferred', 'Transferred'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.name} (UID: {self.unique_id})"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {'Present' if self.present else 'Absent'}"
from .classroom import ClassRoom

Student.add_to_class('classroom', models.ForeignKey(ClassRoom, on_delete=models.CASCADE, null=True, blank=True))



# -------------------------------
# ✅ AttendanceRecord model added
# -------------------------------
from django.db import models

class AttendanceRecord(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"

