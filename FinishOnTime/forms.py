from django import forms
import datetime
from django.contrib.auth.models import User
from FinishOnTime.models import Project, Subtask, Timeslot

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		
class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ('title', 'deadline')
		
class SubtaskForm(forms.ModelForm):
	class Meta:
		model = Subtask
		fields = ('title', 'hours')
		
class TimeslotForm(forms.ModelForm):
	class Meta:
		model = Timeslot
		fields = ('timeslot_start', 'timeslot_end')
