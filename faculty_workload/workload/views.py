from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from .models import Faculty, Workload
from .forms import FacultyForm, WorkloadForm
from django.db.models import Sum, F
import csv
from django.http import HttpResponse
import json
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import UserForm, Profile

from .models import Profile

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Ensure profile is created
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'sign_in.html', {'form': form})



@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



# def signup_view(request):
    # if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        # if form.is_valid():
            # user = form.save()
            # login(request, user)
            # messages.success(request, 'Registration successful.')
            # return redirect('index')
        # else:
            # messages.error(request, 'Registration failed. Please try again.')
    # else:
        # form = UserCreationForm()
    # return render(request, 'sign_in.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})







# Home view
def home(request):
    return render(request, 'index.html')

@login_required
def add_faculty(request):
    if request.method == 'POST':
        # Logic to add a new faculty
        return redirect('index')
    return render(request, 'add_faculty.html')

@login_required
def add_workload(request):
    if request.method == 'POST':
        # Logic to add a new workload
        return redirect('index')
    return render(request, 'add_workload.html')

# Contact Us view
def contact_us(request):
    if request.method == 'POST':
        # Logic to handle contact form submission
        return redirect('index')
    return render(request, 'contact_us.html')

# About Us view
def about_us(request):
    return render(request, 'about_us.html')

# Login view


def index(request):
    faculties = Faculty.objects.all()
    workloads = Workload.objects.all()

    faculty_workloads = (
        Workload.objects
        .values('id', 'faculty__name', 'faculty__department', 'faculty__id')
        .annotate(
            total_teaching_hours=Sum('teaching_hours'),
            total_research_hours=Sum('research_hours'),
            total_admin_hours=Sum('admin_hours')
        )
        .order_by('faculty__name')
    )

    total_workload_hours = Workload.objects.aggregate(
        total_hours=Sum('teaching_hours') + Sum('research_hours') + Sum('admin_hours')
    )['total_hours'] or 0

    for workload in faculty_workloads:
        workload['total_hours'] = (
            workload['total_teaching_hours'] + workload['total_research_hours'] + workload['total_admin_hours']
        )
        workload['score_percentage'] = round((workload['total_hours'] / total_workload_hours) * 100, 2) if total_workload_hours > 0 else 0.0

    max_workload_percentage = max(faculty_workloads, key=lambda x: x['score_percentage']) if faculty_workloads else None

    return render(request, 'index.html', {
        'faculties': faculties,
        'workloads': workloads,
        'faculty_workloads': faculty_workloads,
        'max_workload_percentage': max_workload_percentage
    })

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

def update_workload(request, workload_id):
    workload = get_object_or_404(Workload, id=workload_id)
    if request.method == 'POST':
        form = WorkloadForm(request.POST, instance=workload)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = WorkloadForm(instance=workload)
    return render(request, 'update_workload.html', {'form': form})

def delete_workload(request, workload_id):
    workload = get_object_or_404(Workload, id=workload_id)
    if request.method == 'POST':
        workload.delete()
        return redirect('index')
    return render(request, 'delete_workload.html', {'workload': workload})






def export_workload_data(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="workload_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Faculty Name', 'Department', 'Teaching Hours', 'Research Hours', 'Admin Hours', 'Total Hours', 'Score Percentage'])

    workloads = Workload.objects.values(
        'faculty__name',
        'faculty__department',
        'teaching_hours',
        'research_hours',
        'admin_hours'
    )

    total_workload_hours = Workload.objects.aggregate(
        total_hours=Sum('teaching_hours') + Sum('research_hours') + Sum('admin_hours')
    )['total_hours'] or 0

    for workload in workloads:
        faculty_total_hours = workload['teaching_hours'] + workload['research_hours'] + workload['admin_hours']
        score_percentage = round((faculty_total_hours / total_workload_hours) * 100, 2) if total_workload_hours > 0 else 0.0
        writer.writerow([
            workload['faculty__name'],
            workload['faculty__department'],
            workload['teaching_hours'],
            workload['research_hours'],
            workload['admin_hours'],
            faculty_total_hours,
            score_percentage
        ])

    return response


def workload_table(request):
    faculties = Faculty.objects.all()
    workloads = Workload.objects.all()

    faculty_workloads = []
    for faculty in faculties:
        teaching_hours = workloads.filter(faculty=faculty).aggregate(Sum('teaching_hours'))['teaching_hours__sum'] or 0
        research_hours = workloads.filter(faculty=faculty).aggregate(Sum('research_hours'))['research_hours__sum'] or 0
        admin_hours = workloads.filter(faculty=faculty).aggregate(Sum('admin_hours'))['admin_hours__sum'] or 0
        total_hours = teaching_hours + research_hours + admin_hours
        score = (total_hours / workloads.aggregate(Sum('teaching_hours'))['teaching_hours__sum']) * 100 if total_hours else 0
        faculty_workloads.append({
            'id': faculty.id,
            'name': faculty.name,
            'department': faculty.department,
            'teaching_hours': teaching_hours,
            'research_hours': research_hours,
            'admin_hours': admin_hours,
            'total_hours': total_hours,
            'score': score
        })

    context = {
        'workloads': workloads,
        'faculty_workloads': faculty_workloads,
        'faculty_names': [faculty['name'] for faculty in faculty_workloads],
        'total_hours': [faculty['total_hours'] for faculty in faculty_workloads]
    }
    return render(request, 'workload_table.html', context)



def workload_visualization(request):
    workloads = Workload.objects.all()

    faculty_names = []
    scores = []

    total_hours = workloads.aggregate(
        total_teaching_hours=Sum('teaching_hours'),
        total_research_hours=Sum('research_hours'),
        total_admin_hours=Sum('admin_hours')
    )
    
    total_hours_sum = (
        total_hours['total_teaching_hours'] +
        total_hours['total_research_hours'] +
        total_hours['total_admin_hours']
    )

    for workload in workloads:
        faculty_names.append(workload.faculty.name)
        faculty_total_hours = workload.teaching_hours + workload.research_hours + workload.admin_hours
        score = (faculty_total_hours / total_hours_sum) * 100 if total_hours_sum else 0
        scores.append(score)

    context = {
        'faculty_names': faculty_names,
        'scores': scores,
    }

    return render(request, 'visualization.html', context)