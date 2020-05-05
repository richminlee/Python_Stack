from django.db import models
from datetime import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class loginManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['first_name']) == 0:
            errors['first_name'] = "First name is required."
        elif len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters in length."
        elif not postData['first_name'].isalpha():
            errors['first_name'] = "First name can only contain letters."

        if len(postData['last_name']) == 0:
            errors['last_name'] = "Last name is required."
        elif len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters in length."
        elif not postData['last_name'].isalpha():
            errors['last_name'] = "Last name can only contain letters."

        try:
            if datetime.strptime(postData['birthdate'], "%Y-%m-%d") > datetime.now():
                errors['birthdate'] = "Birthdate needs to be in the past."  
        except:
            errors['birthdate'] = "Not the correct Date format"


        logins = Login.objects.filter(email=postData['email'])
        if len(postData['email']) == 0:
            errors['email'] = "Email address is required."
        elif EMAIL_REGEX.match(postData['email']) == False:
            errors['email'] = "Invalid email address"
        elif len(logins) > 0:
            errors['email'] = "A user with that email address already exists. If that's you, please try and log in."

        if len(postData['password']) == 0:
            errors['password'] = "Password is required"
        elif len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters in length."
        elif postData['password'] != postData['confirmPW']:
            errors['password'] = "Passwords do not match."

        return errors

class BookManager(models.Manager):
    def book_val(self, postData):
        errors = {}

        books = Book.objects.filter(title=postData['title'])
        authors = Book.objects.filter(author=postData['author'])

        if len(postData['title']) < 2:
            errors['title'] = "Book title must be at least 2 characters long."
        if len(books) > 0:
            errors['title'] = "Cannot create duplicate book entry."
        if len(postData['author']) < 4:
            errors['author'] = "Author's name must be at least 4 characters."
        if len(authors) > 0:
            errors['author'] = "An author with that name already exists."
        
        return errors

class Login(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    birthdate = models.DateField()
    alias = models.CharField(max_length = 45,default = 'first_name')
    email = models.CharField(max_length = 90)
    password = models.CharField(max_length = 90)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = loginManager()

class Review(models.Model):
    logged = models.ForeignKey(Login, related_name="reviews", on_delete = models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    logged = models.ForeignKey(Login, related_name="books", on_delete = models.CASCADE)
    title = models.CharField(max_length=75)
    review = models.ManyToManyField(Review, related_name="books")
    author = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()