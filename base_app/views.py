from urllib import request
from django. contrib import messages
from unicodedata import name
from django.shortcuts import render
from django.shortcuts import render, redirect
from base_app.models import *
from datetime import datetime,date
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from io import BytesIO
from django.core.files import File
from django.conf import settings
import qrcode
import os
from django.urls import reverse
from urllib.parse import urlencode

def login(request):
    
    des = designation.objects.get(designation='student')
    if request.method == 'POST':
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=des.id).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['stid'] = member.id
           
            if request.session.has_key('stid'):
                stid = request.session['stid']
            else:
                variable = "dummy"
            pro = user_registration.objects.filter(id=stid)
            return render(request, 'Student_index.html', {'pro':pro})
    return render(request,'login.html')

def Student_index(request):
    return render(request,'Student_index.html')

def Student_applyleave_cards(request):
    return render(request,'Student_applyleave_cards.html')

def Student_leavereq(request):
    if 'stid' in request.session:
        if request.session.has_key('stid'):
            stid = request.session['stid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=stid)
        if request.method == "POST":
            
            
            mem = leave()
            mem.from_date = request.POST.get('from')
            mem.to_date = request.POST.get('to')
            mem.leave_status = request.POST.get('haful')
            mem.reason = request.POST.get('reason')
            mem.user_id = request.POST.get('st_id')
            mem.status = "pending"
            mem.save()
    return render(request,'Student_leavereq.html', {'pro':pro})
    

def Student_reqedleave(request):
    if 'stid' in request.session:
        if request.session.has_key('stid'):
            stid = request.session['stid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=stid)
        var = leave.objects.filter(user_id=stid).order_by('-id')
        return render(request, 'Student_reqedleave.html',{'pro':pro,'var':var}) 
    else:
        return redirect('/')

def Student_progressreport(request):
    return render(request,'Student_progressreport.html')