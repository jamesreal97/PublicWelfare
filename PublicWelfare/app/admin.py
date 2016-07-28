from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *

class ProjectActionInline(admin.TabularInline):
    model=ProjectAction
    extra=1

class ProjectAdmin(admin.ModelAdmin):
    list_display=('ProjectName','ProjectDescription')
    inlines=[ProjectActionInline]

class TeamMemberInline(admin.TabularInline):
    model=TeamMember
    list_display=('TeamMember','TeamMemberRole')
    raw_id_fields=('TeamMember',)
    extra=1

class TeamAdmin(admin.ModelAdmin):
    list_display=('TeamName','TeamDescription')
    inlines=[TeamMemberInline]

class VolunteerInline(admin.StackedInline):
    model=Volunteer
    can_delete=False
    verbose_name_plural='Volunteer'

class VolunteerAdmin(BaseUserAdmin):
    inlines=(VolunteerInline,)

admin.site.register(Team,TeamAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(ProjectAction)
admin.site.register(TeamMemberRole)
admin.site.unregister(User)
admin.site.register(User, VolunteerAdmin)