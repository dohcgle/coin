from django.shortcuts import render
from team.models import Team

def team(request):
    teams = Team.objects.all()
    context = {
        "teams": teams,
    }
    return render(request, 'team/team.html', context)
