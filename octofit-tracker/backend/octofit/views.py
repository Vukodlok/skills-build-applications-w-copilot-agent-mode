from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

@api_view(['GET'])
def api_root(request, format=None):
    codespace_url = "https://effective-orbit-9w56vvqgw92p96-8000.app.github.dev/api"
    local_url = "http://localhost:8000/api"
    return Response({
        'users': f'{codespace_url}/users/',
        'teams': f'{codespace_url}/teams/',
        'activity': f'{codespace_url}/activity/',
        'workouts': f'{codespace_url}/workouts/',
        'leaderboard': f'{codespace_url}/leaderboard/',
        'users_local': f'{local_url}/users/',
        'teams_local': f'{local_url}/teams/',
        'activity_local': f'{local_url}/activity/',
        'workouts_local': f'{local_url}/workouts/',
        'leaderboard_local': f'{local_url}/leaderboard/',
    })

# Copilot agent mode: This file was updated by GitHub Copilot agent mode to add the codespace Django REST API endpoint suffix.
