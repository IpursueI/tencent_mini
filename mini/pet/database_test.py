from pet.models import User
from pet.models import Activity
from pet.models import Participant

act = Activity.objects.filter(activity_introduction= "hello kitty")
