

# Create your views here.

from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render

import json
import smtplib
import base64
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.template import Context, loader
from django.views.generic import TemplateView
from datetime import date, datetime

from calendar import monthrange
from .models import UserProfile
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

@login_required
def home(request):
    context = {}
    user_profile = UserProfile.objects.get(user=request.user)
    month = datetime.now().strftime("%m")
    year = datetime.now().strftime("%Y")
    day = datetime.now().strftime("%d")
    print ("day ", day)
    context.update({'user_profile': user_profile})
    return render(request, 'index.html', context)

def about_us(request):
    context = {}
    return render(request, 'about_us.html', context)

def flight_booking(request):
    context = {}
    return render(request, 'flight_booking.html', context)

def train_booking(request):
    context = {}
    return render(request, 'train_booking.html', context)

def bus_booking(request):
    context = {}
    return render(request, 'bus_booking.html', context)

def fertilizers(request):
    context = {}
    return render(request, 'fertilizers.html', context)

def fuel(request):
    context = {}
    return render(request, 'fuel.html', context)

def recycle(request):
    context = {}
    return render(request, 'recycle.html', context)

def green_invst_kitty(request):
    context = {}
    return render(request, 'green_kitty.html', context)
