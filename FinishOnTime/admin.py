from django.contrib import admin
from FinishOnTime.models import Project, Subtask, Timeslot

# Register your models here.
admin.site.register(Project)
admin.site.register(Subtask)
admin.site.register(Timeslot)
