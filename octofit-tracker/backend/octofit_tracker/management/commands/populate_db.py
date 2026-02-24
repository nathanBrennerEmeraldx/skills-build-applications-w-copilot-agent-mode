from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='hero', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='hero', first_name='Steve', last_name='Rogers'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='hero', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='hero', first_name='Diana', last_name='Prince'),
        ]

        # Create activities
        Activity.objects.create(name='Running', user='ironman', team='Marvel', points=100)
        Activity.objects.create(name='Swimming', user='captainamerica', team='Marvel', points=80)
        Activity.objects.create(name='Cycling', user='batman', team='DC', points=90)
        Activity.objects.create(name='Yoga', user='wonderwoman', team='DC', points=70)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=180)
        Leaderboard.objects.create(team='DC', points=160)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes.', suggested_for='Marvel')
        Workout.objects.create(name='Justice Yoga', description='Yoga for balance and strength.', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
