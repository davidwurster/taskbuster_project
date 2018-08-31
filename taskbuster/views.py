# -*- coding: utf-8 -*-
import datetime
from django.utils.timezone import now
from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def home(request):
    today = datetime.date.today()
    return render(request, "taskbuster/index.html", {'today': today, 'now': now()})


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')