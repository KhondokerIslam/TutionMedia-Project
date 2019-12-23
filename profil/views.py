from django.shortcuts import render, get_object_or_404
from jobs.models import Job
from django.contrib.auth.models import User
# Create your views here.
def profil(request, Tutor_id):

    jobs = get_object_or_404(Job, pk=Tutor_id)
    tutor = User.objects.get(pk=Tutor_id)
    return render(request, 'profil/index.html', {'jobs':jobs, 'tutor':tutor})
