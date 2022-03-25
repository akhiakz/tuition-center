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
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



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

        des = designation.objects.get(designation='manager')
    if request.method == 'POST':
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=des.id).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['mnid'] = member.id
           
            if request.session.has_key('mnid'):
                mnid = request.session['mnid']
            else:
                variable = "dummy"
            pro = user_registration.objects.filter(id=mnid)
            return render(request, 'Man_index.html', {'pro':pro})


        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.get(email=email)
        if user is not None:
            pwd_valid = check_password(password, user.password)
            if pwd_valid:
                request.session['Adm_id'] = user.id
                return redirect('Admin_dashboard')
            else:
                return render(request, 'login.html')

    return render(request,'login.html')

        # email = request.POST.get('email')
        # password = request.POST.get('password')

        # user = User.objects.get(email=email)
        # if user is not None:
        #     pwd_valid = check_password(password, user.password)
        #     if pwd_valid:
        #         request.session['Adm_id'] = user.id
        #         return redirect('Admin_dashboard')
        #     else:
        #         msg_error = "Password is incorrect"
        #         return render(request, 'login.html', {'msg_error': msg_error})


def Student_logout(request):
    if 'stid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def Admin_logout(request):
    if 'adid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

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
    if 'stid' in request.session:
        if request.session.has_key('stid'):
            stid = request.session['stid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=stid)
        progress = progressreport.objects.filter(user_id=stid)
    return render(request,'Student_progressreport.html',{'pro':pro, 'progressreport':progress})





def Admin_index(request):
    return render(request,'Admin_index.html')

def Admin_dashboard(request):
    return render(request,'Admin_dashboard.html')

def logout(request):
    auth.logout(request)
    return redirect('login')



def Man_index(request):
    return render(request,'Man_index.html')

def MAN_Report(request):
    des = designation.objects.all()
    # filter(~Q("admin"))
    return render(request,'MAN_Report.html',{'des':des })

# def MAN_Reportedissue(request):
#     des = designation.objects.all()
#     return render(request,'MAN_Reportedissue.html',{'des':des })

def MAN_ReportedissueShow(request,id):
        designations=designation.objects.get(id=id)
        user=user_registration.objects.filter(designation_id=id)
        reported_issues=reported_issue.objects.all()
        return render(request,'MAN_ReportedissueShow.html',{'designation':designations,'reported_issue':reported_issues,'user_registration':user})

def MAN_rep(request,id):
    
        if request.method == 'POST':
            
            vars = reported_issue.objects.get(id=id)
            vars.reply=request.POST.get('reply')
            vars.status='submitted'
            vars.save()
           
            return redirect('MAN_Report')
       

def MAN_ReportedissueShow1(request,id):
        reported_issues=reported_issue.objects.get(id=id)
        return render(request,'MAN_ReportedissueShow1.html',{'reported_issue':reported_issues})


def MAN_manager_report(request):
    return render(request,'MAN_manager_report.html')

def MAN_Reportissue(request):
    return render(request,'MAN_Reportissue.html')

def MAN_reportsuccess(request):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)
        design=designation.objects.get(designation="admin")
        man = user_registration.objects.get(designation_id=design.id)
        if request.method == 'POST':
            
            vars = reported_issue()
            vars.issue=request.POST.get('MANreportissue')
            vars.reported_date=datetime.now()
            vars.reported_to_id=man.id
            vars.reporter_id=mnid
            vars.status='pending'
            vars.save()
        return render(request, 'MAN_Reportissue.html',{'pro':pro})
    else:
        return redirect('/')
    

def MAN_manger_reportedissues(request):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)
        var = reported_issue.objects.filter(reporter=mnid)
    return render(request,'MAN_manger_reportedissues.html',{'var':var,'pro':pro})


def MAN_manger_reportedissues1(request,id):
        reported_issues=reported_issue.objects.get(id=id)
        return render(request,'MAN_manger_reportedissues1.html',{'reported_issue':reported_issues})





def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Admin_changepassword.html')



            