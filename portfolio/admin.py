from django.contrib import admin

# Register your models here.
from .models import Project, ContactSubmission

admin.site.register(Project)
admin.site.register(ContactSubmission)