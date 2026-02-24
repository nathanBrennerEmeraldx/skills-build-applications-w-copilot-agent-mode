from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='spiderman', email='spiderman@marvel.com')
        self.assertEqual(user.username, 'spiderman')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Avengers')
        self.assertEqual(team.name, 'Avengers')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(name='Jump', user='spiderman', team='Avengers', points=50)
        self.assertEqual(activity.name, 'Jump')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Avengers', points=100)
        self.assertEqual(leaderboard.team, 'Avengers')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Web Swing', description='Swinging workout', suggested_for='Marvel')
        self.assertEqual(workout.name, 'Web Swing')
