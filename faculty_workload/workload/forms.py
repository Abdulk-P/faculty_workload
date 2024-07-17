from django import forms
from .models import Faculty, Workload

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'department']

class WorkloadForm(forms.ModelForm):
    class Meta:
        model = Workload
        fields = ['faculty', 'teaching_hours', 'course', 'research_hours', 'admin_hours']
