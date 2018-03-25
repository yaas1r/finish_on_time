from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Tool for naming urls
from django.template.defaultfilters import slugify

# Datetime tools 
from datetime import datetime

#1. Project
#    Title
#    Created
#    Deadline
#    Progress
class Project(models.Model):
	title = models.CharField(max_length=128, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	deadline = models.DateTimeField()
	progress = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Project, self).save(*args, **kwargs)

	def __str__(self): # For Python 2, use __unicode__ too
		return self.title
#2. Subtask
#    Project
#    Title
#    Deadline
#    Hours
#    Progress
class Subtask(models.Model):
	project = models.ForeignKey(Project)
	title = models.CharField(max_length=128)
	deadline = models.DateTimeField()
	hours = models.IntegerField(default=0)
	progress = models.BooleanField(default=False)

	def __str__(self): # For Python 2, use __unicode__ too
		return self.title
#3. Timeslot
class Timeslot(models.Model):
	timeslot_start = models.DateTimeField()
	timeslot_end = models.DateTimeField()
	timebetween = models.IntegerField()
	def save(self, *args, **kwargs):
		self.timebetween = (self.timeslot_end - self.timeslot_start)
		self.timebetween = int(self.timebetween.days * 24 * 3600 + self.timebetween.seconds)//60
		super(Timeslot, self).save(*args, **kwargs)

	def __str__(self): # For Python 2, use __unicode__ too
		return str(self.timebetween)
