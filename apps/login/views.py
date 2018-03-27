# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import User
from django.contrib import messages
import bcrypt
import re


# Create your views here.
def loginPage(request):
    return render(request, 'login/login.html')

def login(request):
    if User.objects.filter(email = request.POST['username_email']) or User.objects.filter(username = request.POST['username_email']):
        if re.compile(r'(.*?\.com)$').match(request.POST['username_email']):
            print "*********** email check **********"
            user = User.objects.get(email = request.POST['username_email'])
        elif not re.compile(r'(.*?\.com)$').match(request.POST['username_email']):
            print "*********** username check **********"
            user = User.objects.get(username = request.POST['username_email'])
        login_password = request.POST['password'].encode('utf-8')
        hashed = user.hashedpw.encode('utf-8')
        if (request.POST['username_email'] == user.email or request.POST['username_email'] == user.username) and bcrypt.hashpw(login_password, hashed) == hashed:
            print 'Check 3 ***************'
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['username'] = user.username
            print "********* You've successfully logged in ***********"
            return redirect('/{}'.format(user.username))
        else:
            messages.error(request, "Incorrect password for this email", extra_tags='passwordlogin')
            return redirect('/')
    else:
        messages.error(request, "There is no profile associated with this email", extra_tags='emaillogin')
        return redirect('/')

def register(request, method='POST'): #create
    request.session['first_name'] = request.POST['first_name']
    errors = User.objects.basic_validator(request.POST)
    print 'errors', errors
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    password = request.POST['password'].encode('utf-8')
    print "password", password
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(12))
    print "hash", hashed
    user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'], 
        email = request.POST['email'], 
        username = request.POST['username'],
        hashedpw = hashed
    )
    request.session['id'] = user.id
    request.session['first_name'] = user.first_name
    request.session['username'] = user.username
    return redirect('/{}'.format(user.username))

def logout(request):
    request.session['first_name'] = None
    print "********* You've successfully logged out **********"
    print request.session['first_name']
    return redirect('/')