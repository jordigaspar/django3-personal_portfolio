from django.contrib import admin
from .models import Project # ----- Import de db/model Project to the admin page

admin.site.register(Project)
