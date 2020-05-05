from django.db import models
from datetime import datetime

class showManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 character"
        try:
            if datetime.strptime(postData['release_date'], "%Y-%m-%d") > datetime.now():
                errors['release_date'] = "Release date needs to be in the past."  
        except:
            errors['release_date'] = "Not the correct Date format"
        if len(postData['description']) > 0 and len(postData['description']) < 10:
            errors['description'] = "Description should be at least 10 characters"
        Shows = show.objects.filter(title=postData['title'])
        if len(Shows) > 0:
            errors['title_taken'] = "Show with that title already exists."
        return errors
    def basic_validatory(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 character"
        try:
            if datetime.strptime(postData['release_date'], "%Y-%m-%d") > datetime.now():
                errors['release_date'] = "Release date needs to be in the past."  
        except:
            errors['release_date'] = "Not the correct Date format"  
        if len(postData['description']) > 0 and len(postData['description']) < 10:
            errors['description'] = "Description should be at least 10 characters"
        return errors



class show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = showManager()