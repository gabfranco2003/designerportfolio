from django.contrib import admin
from .models import ContactInfo, Project, Skill, Education, Experience  # Import the model

admin.site.register(ContactInfo)
admin.site.register(Project)  # Register the model
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)