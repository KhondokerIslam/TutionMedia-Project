from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from django.utils import timezone
from django.contrib.auth.models import User

def home(request):
    subjects = {'M':'Math', 'E':'English', 'B':'Biology', 'P':'Physics', 'C':'Chemistry', 'I':'ICT', 
                'BN':'Bangla', 'CM':'Computer'}
    days = [1,2,3,4,5,6,7]
    return render(request, 'jobs/home.html', {'subjects':subjects,'days':days} )


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


def search(request):
    if request.method == 'POST':
        _class, name, tution_type, gender, subject, medium, institution = ('',)*7

        if request.POST.get('class'):
            _class = request.POST.get('class')
            if(_class == 'EMNI'): 
                _class = ''
        if request.POST['name']:
            name = request.POS['name']
        if request.POST.get('tutiontype'):
            tution_type = request.POST.get('tutiontype')
            if(tution_type == 'EMNI'): 
                tution_type = ''
        if request.POST.get('gender'):
            gender = request.POST.get('gender')
            if(gender == 'EMNI'): 
                gender = ''

        # I have to convert 'medium' and 'subject' from list to string
        # Because in database it is stored as a string
        if request.POST.getlist('medium'):
            mediums = request.POST.getlist('medium')
            medium_len = len(mediums)
            medium = ''
            for i in range(0, medium_len - 1):
                medium += mediums[i] + ','
            medium += mediums[medium_len - 1]
        if request.POST.getlist('subject'):
            subjects = request.POST.getlist('subject')
            sub_len = len(subjects)
            subject = ''
            for i in range(0, sub_len - 1):
                subject += subjects[i] + ','
            subject += subjects[sub_len - 1]
        if request.POST['institution']:
            institution = request.POST['institution']
        
        # Got a set of profile object
        profiles = Job.objects.all().filter(
            Class__icontains = _class
            ).filter(
                Gender__icontains = gender
                ).filter(
                    Tution_Type__icontains = tution_type
                    ).filter(
                        Subject__icontains = subject
                        ).filter(
                            Medium__icontains = medium
                        ).filter(
                            Institution__icontains = institution
                        ).order_by('Tutor_id')

        # Iterate over all the profile object and make tutor id list
        # to get Tutor objects for all the profiles
        tutor_id = []
        for profile in profiles:
            tutor_id.append(profile.Tutor_id)

        tutors = User.objects.all().filter(pk__in = tutor_id).order_by('id')

        # For multiple variable iterate
        zippedList = zip(profiles, tutors)
        return render(request, 'jobs/search2.html', {'profiles':profiles, 'tutors':tutors, 'zippedlist':zippedList} )


def RateList(request):
    queryset = Job.objects.filter(ratings__isnull=False).order_by('ratings__average')
    context= {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, 'jobs/index.html', context)