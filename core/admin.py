from django.contrib import admin
from .models import Domain, Project, SkillGroup, Skill, Certification

admin.site.register(Domain)
admin.site.register(Project)
admin.site.register(SkillGroup)
admin.site.register(Skill)
admin.site.register(Certification)