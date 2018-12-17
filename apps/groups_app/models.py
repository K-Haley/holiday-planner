from django.db import models

class ValidateGroups(models.Manager):
    def validateGroups(self, postData):
        errors = {}
        if 'groupname' in postData:
            if len(postData['groupname']) < 2:
                errors["firstname"] = "The name of your group must contain at least 2 characters"
        return errors

class Groups(models.Model):
    group_name = models.CharField(max_length=255)
    members = models.ManyToManyField('login_app.Users', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ValidateGroups()

class Messages(models.Model):
    message = models.CharField(max_length=255)
    posted_by = models.ForeignKey('login_app.Users', on_delete=models.CASCADE)
    groupid = models.ForeignKey(Groups, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)