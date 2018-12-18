from django.db import models
import re
import bcrypt


class Validate(models.Manager):
    def validate(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        PASSWORD_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{4,16}$')
        errors = {}
        x = Users.objects.all()
        for i in x:
            if i.email == postData['email']:
                errors["emailUnique"] = "Email has already been used"
        for j in x:
            if j.user_name == postData['username']:
                errors["usernameUnique"] = "username has already been used"
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
        if 'item' in postData:
            if len(postData['itemname']) < 2:
                errors["item"] = "The item's names must contain at least 2 characters"
        return errors

    def login_validator(self, postData):
        errors = {}
        user = Users.objects.filter(user_name=postData['username'].lower())
        if len(user) < 1:
            errors["wrong"] = "username or password wrong"
        elif bcrypt.checkpw(postData['password1'].encode(), user[0].password.encode()):
            print("passwords match")
        else:
            errors["wrong"] = "username or password wrong"
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

class Items(models.Model):
    item = models.CharField(max_length=255)
    taken = models.BooleanField(default=False)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validate()