from django.db import models
from datetime import datetime
import re

class loginManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name should be at least 2 characters"
        try:
            if datetime.strptime(postData['birthdate'], "%Y-%m-%d") > datetime.now():
                errors['birthdate'] = "Birthdate needs to be in the past."  
        except:
            errors['birthdate'] = "Not the correct Date format"
        logins = Login.objects.filter(email=postData['email'])
        if len(logins) > 0:
            errors['email_taken'] = "Account with that email already exists."
        passwd = postData['password']
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)             
        mat = re.search(pat, passwd) 
        if mat:
            pass
        else: 
            errors['password_invalid'] = "Password invalid !!"
        if postData['confirmPW'] != postData['password']:
            errors['confirmPW'] = "Your Passwords do not match"
        return errors

class Login(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    birthdate = models.DateField()
    email = models.CharField(max_length = 90)
    password = models.CharField(max_length = 90)
    confirmPW = models.CharField(max_length = 90)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = loginManager()