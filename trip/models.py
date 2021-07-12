from django.db import models
from login.models import User
#from datetime import datetime

# Create your models here.
class TripManager(models.Model):

    def validate(self, form_data):
        errors ={}
        if len(form_data['destination']) < 3:
            errors['destination'] = "Destination field must have at least 3 characters."
        
        #elif (datetime.strptime(form_data['start_date'],"%Y-%m-%d") < datetime.now()):
            #errors['start_date'] = "Date must be in the future."

        if len(form_data['start_date']) < 1:
            errors['start_date'] = "Date field is required!"
       
        if len(form_data['plan']) < 1:
            errors['plan'] = "Plan field is required!"
        print(form_data)

        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.CharField(max_length=255, default=None)
    planner = models.ForeignKey(User, related_name='planned_trips', on_delete=models.CASCADE)
    travelers = models.ManyToManyField(User, related_name="travelers")
    #created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    #updated_at = models.DateTimeField(auto_now=True)

    #objects = TripManager()


