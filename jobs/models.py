from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    Class = models.CharField(max_length = 50)
    Subject = models.CharField(max_length = 50)
    Location = models.TextField()
    Days = models.IntegerField()
    url = models.TextField()
    Salary = models.TextField()
    Post_date = models.DateTimeField()
    interested_total = models.IntegerField()
    poster = models.ForeignKey(User, on_delete =models.CASCADE )

    def Post_date_Pretty(self):
        return self.Post_date.strftime('%b %e %Y')
