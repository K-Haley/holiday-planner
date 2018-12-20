from django.db import models

class ValidateGroups(models.Manager):
    def validateGroups(self, postData):
        errors = {}
        if 'groupname' in postData:
            if len(postData['groupname']) < 2:
                errors["groupname"] = "The name of your group must contain at least 2 characters"
            if postData['groupdesc'] != '':
                if len(postData['groupdesc']) < 10:
                    errors["groupdesc"] = "If included, a description must be at least 10 characters"
        if 'messagetext' in postData:
            if len(postData['messagetext']) < 1:
                errors["messagetext"] = "Your message must contain at least 1 character"
        return errors

class Groups(models.Model):
    group_name = models.CharField(max_length=255)
    group_desc = models.TextField(max_length=1000)
    group_owner = models.ForeignKey('login_app.Users', on_delete=models.CASCADE, related_name='owner')
    members = models.ManyToManyField('login_app.Users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ValidateGroups()

class PMessages(models.Model):
    message = models.CharField(max_length=255)
    posted_by = models.ForeignKey('login_app.Users', on_delete=models.CASCADE)
    sent_to = models.ForeignKey('login_app.Users', on_delete=models.CASCADE, related_name='sent_to')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ValidateGroups()