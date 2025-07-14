from django import forms
from .models import Student

class AttendanceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        students = Student.objects.all()
        for student in students:
            self.fields[f'student_{student.id}'] = forms.BooleanField(
                label=student.name,
                required=False,
                initial=True
            )
