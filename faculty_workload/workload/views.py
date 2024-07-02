from django.shortcuts import render, redirect
from .models import Faculty, Workload
from .forms import FacultyForm, WorkloadForm

def index(request):
    faculties = Faculty.objects.all()
    workloads = Workload.objects.all()
    return render(request, 'index.html', {'faculties': faculties, 'workloads': workloads})

def add_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FacultyForm()
    return render(request, 'add_faculty.html', {'form': form})

def add_workload(request):
    if request.method == 'POST':
        form = WorkloadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = WorkloadForm()
    return render(request, 'add_workload.html', {'form': form})
