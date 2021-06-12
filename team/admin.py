from django.contrib import admin
from team.models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'is_active')
    prepopulated_fields = {'facebook': ['full_name'], 'twitter': ['full_name'], 'linkedin': ['full_name'], 'instagram': ['full_name']}