from django.contrib import admin
from .models import Blog # ----- Import de db/model Project to the admin page

admin.site.register(Blog)
