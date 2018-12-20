from django.db import models
import datetime

class ValidateEvents(models.Manager):
    def validateEvents(self, postData):
        errors = {}
        if 'eventname' in postData:
            if len(postData['eventname']) < 2:
                errors["eventname"] = "The name of your event must contain at least 2 characters"
            if len(postData['eventdesc']) < 10:
                errors["eventdesc"] = "Your event description must contain at least 10 characters"
            if postData['eventdate'] == '':
                errors["noeventdate"] = "You must enter a date for the event"
            if postData['eventdate'] != '':
                todaysDate = datetime.datetime.today()
                userDate = datetime.datetime.strptime(postData['eventdate'], '%Y-%m-%d')
                if todaysDate >= userDate:
                    errors["eventdate"] = "Your event must be in the future"
            if postData['eventtime'] == '':
                errors["eventtime"] = "You must enter a time for the event"
            if len(postData['eventlocation']) < 5:
                errors["eventlocation"] = "You must enter a valid location for the event"
        if 'foodname' in postData:
             if len(postData['foodname']) < 2:
                errors["foodname"] = "The item's names must contain at least 2 characters"
        return errors

class Events(models.Model):
    event_name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    has_food = models.BooleanField(default=False)
    groupid = models.ForeignKey('groups_app.Groups', on_delete=models.CASCADE)
    created_by = models.ForeignKey('login_app.Users', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ValidateEvents()

class Foods(models.Model):
    food_item = models.CharField(max_length=255)
    eventid = models.ForeignKey(Events, blank=True, null=True, on_delete=models.CASCADE)
    brought_by = models.ForeignKey('login_app.Users', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ValidateEvents()