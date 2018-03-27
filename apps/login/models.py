# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        #validate first name
        if len(postData['first_name']) <= 2 or not postData['first_name'].isalpha():
            errors['first_name'] = "First name must be more than 2 characters"
        #validate last name
        if len(postData['last_name']) <= 2 or postData['last_name'].isdigit():
            errors['last_name'] = "Last name must be more than 2 characters"
        #validate email
        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = 'Please provide a valid email'
        else:
            if User.objects.filter(email = postData['email']):
                errors['email'] = 'This email already exists'
        #validate username
        if User.objects.filter(username = postData['username']):
            errors['username'] = 'This username already exists'
        #validate password 
        pwc = postData['password_confirm']
        if len(postData['password']) < 8: 
            errors['password'] = "Password needs to be more than 8 characters"
        elif postData['password'] != pwc:
            errors['password_confirm'] = "Passwords did not match"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    hashedpw = models.TextField()
    objects = UserManager()