from django.contrib import admin
from .models import Project, Experience, Certification, Blog, Education, Skill

admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Certification)
admin.site.register(Blog)
admin.site.register(Education)
admin.site.register(Skill)