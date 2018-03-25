from django.shortcuts import render

# Dynamic data
# Import the Category model
from FinishOnTime.models import User, Project, Subtask, Timeslot

from FinishOnTime.forms import UserForm

from FinishOnTime.forms import ProjectForm, SubtaskForm, TimeslotForm

from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from datetime import datetime

# Create your views here.
from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage': 'Index page'}
	return render(request, 'FinishOnTime/index.html', context_dict)
@login_required
def library(request):
	context_dict = {}
	return render(request, 'FinishOnTime/library.html', context_dict)
@login_required
def project(request):
	context_dict = {}
	return render(request, 'FinishOnTime/project.html', context_dict)
@login_required
def add(request):
	form = ProjectForm()
	# A HTTP POST?
	if request.method == 'POST':
		form = ProjectForm(request.POST)
		# Have we been provided with a valid form?
		if form.is_valid():
			# Save the new category to the database.
			form.save(commit=True)
			# Now that the category is saved
			# We could give a confirmation message
			# But since the most recent category added is on the index page
			# Then we can direct the user back to the index page.
			return index(request)
		else:
			# The supplied form contained errors -
			# just print them to the terminal.
			print(form.errors)
	# Will handle the bad form, new form, or no form supplied cases.
	# Render the form with error messages (if any).
	return render(request, 'FinishOnTime/add.html', {'form':form})
@login_required
def edit(request):
	context_dict = {}
	return render(request, 'FinishOnTime/edit.html', context_dict)
def about(request):
	context_dict = {}
	return render(request, 'FinishOnTime/about.html', context_dict)
