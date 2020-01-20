from django.shortcuts import render, get_object_or_404
from jobs.models import Job
from django.contrib.auth.models import User
# Create your views here.
def profil(request, Tutor_id):
    votes = 0
    if ('star1').checked in request.POST:
        votes += 1
    if ('star2').checked in request.POST:
        votes += 1
    if ('star3').checked in request.POST:
        votes += 1
    if ('star4').checked in request.POST:
        votes += 1
    if ('star5').checked in request.POST:
        votes += 1
    
    profile = get_object_or_404(Job, pk=Tutor_id)
    tutor = User.objects.get(pk=Tutor_id)
    return render(request, 'profil/profile.html', {'profile':profile, 'tutor':tutor})
