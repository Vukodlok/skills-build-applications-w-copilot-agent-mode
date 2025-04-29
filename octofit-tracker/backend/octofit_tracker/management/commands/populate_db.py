# Copilot agent mode: This file was generated and updated by GitHub Copilot agent mode to add test data for the OctoFit Tracker app.

from django.core.management.base import BaseCommand
from octofit.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams
        team1 = Team.objects.create(name='Team Octopus', members=[user1.email, user2.email])
        team2 = Team.objects.create(name='Team Kraken', members=[user3.email])

        # Activities
        Activity.objects.create(user=user1, activity_type='running', duration=30, date=timezone.now())
        Activity.objects.create(user=user2, activity_type='walking', duration=45, date=timezone.now())
        Activity.objects.create(user=user3, activity_type='cycling', duration=60, date=timezone.now())

        # Workouts
        Workout.objects.create(user=user1, workout_type='strength', details={'sets': 3, 'reps': 10}, date=timezone.now())
        Workout.objects.create(user=user2, workout_type='cardio', details={'distance': 5}, date=timezone.now())

        # Leaderboard
        Leaderboard.objects.create(team=team1, points=100, rank=1)
        Leaderboard.objects.create(team=team2, points=80, rank=2)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
