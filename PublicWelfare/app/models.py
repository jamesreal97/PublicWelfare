"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Team(models.Model):
    TeamName=models.CharField(max_length=200)
    TeamDescription=models.CharField(max_length=500)
    def __str__(self):
        return self.TeamName

class TeamMemberRole(models.Model):
    RoleName=models.CharField(max_length=200)
    def __str__(self):
        return self.RoleName

class TeamMember(models.Model):
    Team=models.ForeignKey(Team)
    TeamMember=models.ForeignKey(User)
    TeamMemberRole=models.ForeignKey(TeamMemberRole)
    def __str__(self):
        return '%s'%self.TeamMember

class Project(models.Model):
    ProjectName=models.CharField(max_length=200)
    ProjectDescription=models.CharField(max_length=1000)
    pubDate=models.DateTimeField('date published')
    def __str__(self):
        return self.ProjectName

class ProjectAction(models.Model):
    Project=models.ForeignKey(Project,on_delete=models.CASCADE)
    ActionDescription=models.CharField(max_length=1000)
    pubDate=models.DateTimeField('date published')
    ActionStartDate=models.DateTimeField('Action Start Date')
    ActionEndDate=models.DateTimeField('Action End Date')

class VolunteerSkill(models.Model):
    skill=models.CharField(max_length=20)

class Volunteer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    office=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    section=models.CharField(max_length=50)
    sex=models.CharField(max_length=10)
    isCPC=models.BooleanField()
    title=models.CharField(max_length=50)
    skills=models.ManyToManyField(VolunteerSkill)
    photo=models.URLField()
    comments=models.TextField()



