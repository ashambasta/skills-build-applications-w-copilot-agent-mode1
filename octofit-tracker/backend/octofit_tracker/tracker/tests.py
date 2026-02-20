from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
	def test_create_team(self):
		team = Team.objects.create(name="Marvel", description="Marvel superheroes")
		self.assertEqual(str(team), "Marvel")

	def test_create_user(self):
		team = Team.objects.create(name="DC", description="DC superheroes")
		user = User.objects.create(name="Clark Kent", email="clark@dc.com", team=team)
		self.assertEqual(str(user), "Clark Kent")

	def test_create_activity(self):
		team = Team.objects.create(name="Marvel")
		user = User.objects.create(name="Tony Stark", email="tony@marvel.com", team=team)
		activity = Activity.objects.create(user=user, activity_type="Running", duration=30, date="2024-01-01")
		self.assertIn("Tony Stark", str(activity))

	def test_create_workout(self):
		workout = Workout.objects.create(name="Pushups", description="Upper body strength")
		self.assertEqual(str(workout), "Pushups")

	def test_create_leaderboard(self):
		team = Team.objects.create(name="Marvel")
		user = User.objects.create(name="Peter Parker", email="peter@marvel.com", team=team)
		leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
		self.assertIn("Peter Parker", str(leaderboard))
