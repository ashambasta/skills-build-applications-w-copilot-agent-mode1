from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=tony, activity_type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, activity_type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, activity_type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, activity_type='Flying', duration=120, date=timezone.now().date())

        # Create workouts
        workout1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        workout2 = Workout.objects.create(name='Sprints', description='Speed training')
        workout1.suggested_for.set([tony, steve])
        workout2.suggested_for.set([bruce, clark])

        # Create leaderboard
        Leaderboard.objects.create(user=tony, score=150, rank=1)
        Leaderboard.objects.create(user=steve, score=120, rank=2)
        Leaderboard.objects.create(user=bruce, score=110, rank=3)
        Leaderboard.objects.create(user=clark, score=100, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
