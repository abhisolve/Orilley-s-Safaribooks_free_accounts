from background_task import background
from django.contrib.auth.models import User
from django.utils import timezone

@background(schedule=1)
def create_account():
    pass


create_account(repeat=777600, repeat_until=timezone.now()+timezone.timedelta(days=1))