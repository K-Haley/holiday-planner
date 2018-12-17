from django.db import models
import re

class Validate(models.Manager):
    def validate(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        PASSWORD_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{4,16}$')
        errors = {}
        x = Users.objects.all()
        for i in x:
            if i.email == postData['email']:
                errors["emailUnique"] = "Email has already been used"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please enter a valid email address: example@example.com"
        if len(postData['fname']) < 2:
            errors["firstname"] = "First name must contain least 2 characters"
        if len(postData['lname']) < 2:
            errors["lastname"] = "Last name must contain at least 2 characters"
        if postData['password1'] == '':
            errors["nopassword"] = "You must enter a password"
        if postData['password1'] != postData['password2']:
            errors["passwordmatch"] = "Passwords must match"
        if not PASSWORD_REGEX.match(postData['password1']):
            errors["password"] = "Password must be between 4 and 16 characters, and include at least one lowercase, one uppercase and one number"
        return errors

class Users(models.Model):
    user_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validate()