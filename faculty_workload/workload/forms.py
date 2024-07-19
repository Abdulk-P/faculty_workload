from django import forms
from .models import Faculty, Workload
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'department']

class WorkloadForm(forms.ModelForm):
    class Meta:
        model = Workload
        fields = ['faculty', 'teaching_hours', 'course', 'research_hours', 'admin_hours']



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']





