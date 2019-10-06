from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from django.utils import timezone

def home(request):
    job = Job.objects
    return render(request, 'jobs/home.html', {'Job':job} )

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['Class'] and request.POST['Subject'] and request.POST['location'] and  request.POST['days'] and request.POST['url'] and request.POST['Salary']:
            job = Job()
            job.Class = request.POST['Class']
            job.Subject = request.POST['Subject']
            job.Location =  request.POST['location']
            job.Days=request.POST['days']
            job.url= request.POST['url']
            job.Salary = request.POST['Salary']
            job.Post_date = timezone.datetime.now()
            job.poster = request.user
            job.interested_total = 0
            job.save()
            return redirect('home')
        else:
            _class = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
            subjects = ['Math', 'English', 'Biology', 'Physics', 'Chemistry']
            days = [1,2,3,4,5,6,7]
            return render(request, 'jobs/create.html', {'grade': _class,'subjects':subjects,'days':days, 'error':'All Fields are required.' } )

    else:
        _class = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
        subjects = ['Math', 'English', 'Biology', 'Physics', 'Chemistry']
        days = [1,2,3,4,5,6,7]
        return render(request, 'jobs/create.html', {'grade': _class,'subjects':subjects,'days':days} )
