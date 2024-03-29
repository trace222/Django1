from django.db import models
from django.forms import ModelForm
# Create your models here.
class Candidate(models.Model):
    name=models.CharField(max_length=10)
    introduction=models.TextField()
    area=models.CharField(max_length=15)
    partynum=models.IntegerField(default=1)
    def __str__(self):
        return self.name

class Poll(models.Model):
    start_date= models.DateTimeField()
    end_date= models.DateTimeField()
    area=models.CharField(max_length=15)

class Choice(models.Model):
    poll=models.ForeignKey(Poll, on_delete = models.CASCADE)
    candidate=models.ForeignKey(Candidate, on_delete = models.CASCADE)
    votes=models.IntegerField(default=1)

class Boardlist(models.Model):
    name=models.CharField(max_length=10)
    introduction=models.TextField()

class Post(models.Model):
    name=models.CharField(max_length=10)
    introduction=models.TextField()

