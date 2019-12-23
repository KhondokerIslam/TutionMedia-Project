from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from datetime import date

class Job(models.Model):

    Class_Catagory = [
        ('PR', 'Primary (1-5)'),
        ('JU', 'Junior (6-8)'),
        ('SSC', 'Scondary (9-10)'),
        ('HSC', 'Higher Secondary (11-12)')
    ]

    Subject_Choices = [
        ('M', 'Math'),
        ('E', 'English'),
        ('P', 'Physics'),
        ('C', 'Chemistry'),
        ('B', 'Biology'),
        ('BN', 'Bangla'),
        ('I', 'ICT'),
        ('CM', 'Computer')
    ]

    Medium_Choices = [
        ('BM', 'Bangla Medium'),
        ('EM', 'English Medium'),
        ('EV', 'English Version(National Curriculam)')
    ]

    TUTION_CHOICES = (
        ('PR', 'Private'),
        ('BC', 'Batch'),
        ('PB', 'Both Private and Batch')
    )

    Tutor = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    Profile_Pic = models.ImageField(default='/images/propic avater.jpg', upload_to = 'profile_pic/')
    Gender = models.CharField(default='', max_length = 10)
    Phone = models.CharField(default='', max_length = 15)
    DOB = models.DateField(default=date(1111, 11, 11))
    Address = models.TextField(default='', max_length = 150)
    Religion = models.CharField(default='', max_length = 10)
    Class = MultiSelectField(choices=Class_Catagory, max_choices=3, max_length=15)
    Subject = MultiSelectField(choices=Subject_Choices, max_length=100)
    Medium = MultiSelectField(default='', choices=Medium_Choices, max_length=15)
    Location = models.TextField(max_length = 100)
    Days = models.IntegerField()
    Tution_Type = models.CharField(choices=TUTION_CHOICES, default='', max_length=15)
    Salary = models.TextField()
    Institution = models.CharField(default='', max_length = 100)
    Degree = models.CharField(default='', max_length = 100)
    MySubject = models.CharField(default='', max_length = 100)
    Registration = models.CharField(default='', max_length = 30)
    Vote = models.IntegerField(default=0)

