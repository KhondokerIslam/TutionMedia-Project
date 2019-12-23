from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from django.utils import timezone

def home(request):
    
    return render(request, 'jobs/home.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['class'] and request.POST['subject'] and request.POST['location'] and  request.POST['days'] and request.POST['salary']:
            job = Job()
            job.Profile_Pic = request.FILES['propic']
            job.Gender = request.POST.get('gender')
            job.Phone = request.POST['phone']
            job.DOB = request.POST['birthdate']
            job.Address = request.POST['address']
            job.Religion = request.POST['religion']
            job.Class = request.POST.getlist('class')
            job.Subject = request.POST.getlist('subject')
            job.Location =  request.POST['location']
            job.Days = request.POST['days']
            job.Medium = request.POST.getlist('medium')
            job.Salary = request.POST['salary']
            job.Tution_Type = request.POST['tutiontype']
            job.Degree = request.POST['degree']
            job.Institution = request.POST['institution']
            job.MySubject = request.POST['mysubject']
            job.Registration = request.POST['regno']
            job.Tutor = request.user
            job.save()
            return redirect('home')
        else:
            # _class = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
            # _class = ['1-5', '5-8', '5-10', '5-12', '9-10', '9-12', '11-12']
            subjects = {'M':'Math', 'E':'English', 'B':'Biology', 'P':'Physics', 'C':'Chemistry', 'I':'ICT', 
                        'BN':'Bangla', 'CM':'Computer'}
            days = [1,2,3,4,5,6,7]
            return render(request, 'jobs/create.html', {'subjects':subjects,'days':days, 'error':'All Fields are required.' } )

    else:
        # _class = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
        subjects = {'M':'Math', 'E':'English', 'B':'Biology', 'P':'Physics', 'C':'Chemistry', 'I':'ICT', 
                    'BN':'Bangla', 'CM':'Computer'}
        days = [1,2,3,4,5,6,7]
        return render(request, 'jobs/create.html', {'subjects':subjects,'days':days} )
