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
    des1 = designation.objects.get(designation='manager')
    des3 = designation.objects.get(designation='staff')
    des4 = designation.objects.get(designation='account')

    if request.method == 'POST':
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=des.id).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['stid'] = member.id
            request.session['usernametrns1'] = member.designation_id
           
            if request.session.has_key('stid'):
                stid = request.session['stid']
            else:
                variable = "dummy"
            pro = user_registration.objects.filter(id=stid)
            return render(request, 'Student_index.html', {'pro':pro})

    
    
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=des1.id).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['mnid'] = member.id

           
            if request.session.has_key('mnid'):
                mnid = request.session['mnid']
            else:
                variable = "dummy"
            pro = user_registration.objects.filter(id=mnid)
            return render(request, 'Man_index.html', {'pro':pro})

    
    
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=des3.id).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['sfid'] = member.id
            request.session['usernametrns2'] = member.designation_id
           
            if request.session.has_key('sfid'):
                sfid = request.session['sfid']
            else:
                variable = "dummy"
            pro = user_registration.objects.filter(id=sfid)
            return render(request, 'Staff_index.html', {'pro':pro})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=des4.id).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['accid'] = member.id

           
            if request.session.has_key('accid'):
                accid = request.session['accid']
            else:
                variable = "dummy"
            pro = user_registration.objects.filter(id=accid)
            return render(request, 'Acc_index.html', {'pro':pro})


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
    




def Admin_index(request):
    return render(request,'Admin_index.html')

def Admin_dashboard(request):
    return render(request,'Admin_dashboard.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

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
    if 'stid' in request.session:
        if request.session.has_key('stid'):
            stid = request.session['stid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=stid)
        return render(request,'Student_index.html',{'pro':pro})
    else:
        return redirect('/')

def Student_applyleave_cards(request):
    if 'stid' in request.session:
        if request.session.has_key('stid'):
            stid = request.session['stid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=stid)
        return render(request,'Student_applyleave_cards.html',{'pro':pro})
    else:
        return redirect('/')

def Student_leavereq(request):
    if 'stid' in request.session:
        if request.session.has_key('stid'):
            stid = request.session['stid']
        if request.session.has_key('usernametrns1'):
            usernametrns1 = request.session['usernametrns1']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=stid)
        pro2 = user_registration.objects.get(id=stid)
        if request.method == "POST":
            
            
            mem = leave()
            mem.from_date = request.POST.get('from')
            mem.to_date = request.POST.get('to')
            mem.leave_status = request.POST.get('haful')
            mem.reason = request.POST.get('reason')
            mem.user = pro2
            mem.designation_id = usernametrns1
            mem.status = "pending"
            mem.save()
        return render(request,'Student_leavereq.html', {'pro':pro})
    else:
        return redirect('/')
    

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
    else:
        return redirect('/')









def Man_index(request):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)
        return render(request,'Man_index.html',{'pro':pro})
    else:
        return redirect('/')

def MAN_Report(request):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)
        des = designation.objects.all()
    # filter(~Q("admin"))
        return render(request,'MAN_Report.html',{'des':des,'pro':pro})
    else:
        return redirect('/')

# def MAN_Reportedissue(request):
#     des = designation.objects.all()
#     return render(request,'MAN_Reportedissue.html',{'des':des })

def MAN_ReportedissueShow(request,id):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)
        designations=designation.objects.get(id=id)
        user=user_registration.objects.filter(designation_id=id)
        reported_issues=reported_issue.objects.all()
        return render(request,'MAN_ReportedissueShow.html',{'pro':pro,'designation':designations,'reported_issue':reported_issues,'user_registration':user})
    else:
        return redirect('/')

def MAN_rep(request,id):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)
        if request.method == 'POST':
            
            vars = reported_issue.objects.get(id=id)
            vars.reply=request.POST.get('reply')
            vars.status='submitted'
            vars.save()
           
            return redirect('MAN_Report')
    else:
        return redirect('/')  

def MAN_ReportedissueShow1(request,id):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)
        reported_issues=reported_issue.objects.get(id=id)
        return render(request,'MAN_ReportedissueShow1.html',{'pro':pro,'reported_issue':reported_issues})
    else:
        return redirect('/')


def MAN_manager_report(request):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)
        return render(request,'MAN_manager_report.html',{'pro':pro})
    else:
        return redirect('/')

def MAN_Reportissue(request):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)
        return render(request,'MAN_Reportissue.html',{'pro':pro})
    else:
        return redirect('/')

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
    else:
        return redirect('/')


def MAN_manger_reportedissues1(request,id):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)
        reported_issues=reported_issue.objects.get(id=id)
        return render(request,'MAN_manger_reportedissues1.html',{'pro':pro,'reported_issue':reported_issues})
    else:
        return redirect('/')





def superadmin_changepwd(request):
        if request.method == 'POST':

            newPassword = request.POST.get('newPassword')
            confirmPassword = request.POST.get('confirmPassword')

            user = User.objects.get(is_superuser=True)
            if newPassword == confirmPassword:
                user.set_password(newPassword)
                user.save()
                msg_success = "Password has been changed successfully"
                return render(request, 'Admin_changepassword.html', {'msg_success': msg_success})
            else:
                msg_error = "Password does not match"
                return render(request, 'Admin_changepassword.html', {'msg_error': msg_error})
        return render(request,'Admin_changepassword.html')
  


# subeesh work      

def Staff_index(request):
    if 'sfid' in request.session:
        if request.session.has_key('sfid'):
            sfid = request.session['sfid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=sfid)
        return render(request, 'Staff_index.html',{'pro':pro})
    else:
        return redirect('/')

def Staff_leave(request):
    if 'sfid' in request.session:
        if request.session.has_key('sfid'):
            sfid = request.session['sfid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=sfid)
        return render(request, 'Staff_leave.html',{'pro':pro})
    else:
        return redirect('/')

def Staff_Student_det(request):
    if 'sfid' in request.session:
        if request.session.has_key('sfid'):
            sfid = request.session['sfid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=sfid)
        return render(request, 'Staff_Student_det.html',{'pro':pro})
    else:
        return redirect('/')

def Staff_apply_leave(request):  
    if 'sfid' in request.session:
        if request.session.has_key('sfid'):
            sfid = request.session['sfid']
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=sfid)
        pro2 = user_registration.objects.get(id=sfid)
        if request.method == "POST":
            
            
            mem = leave()
            mem.from_date = request.POST.get('from')
            mem.to_date = request.POST.get('to')
            mem.leave_status = request.POST.get('haful')
            mem.reason = request.POST.get('reason')
            mem.user = pro2
            mem.designation_id = usernametrns2
            mem.status = "pending"
            mem.save()
        return render(request, 'Staff_apply_leave.html',{'pro':pro})
    else:
        return redirect('/')

def Staff_Req_leave(request):
    if 'sfid' in request.session:
        if request.session.has_key('sfid'):
            sfid = request.session['sfid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=sfid)
        var = leave.objects.filter(user_id=sfid).order_by("-id")
        return render(request, 'Staff_Req_leave.html',{'pro':pro,'var':var})
    else:
        return redirect('/')

# def Student_profiledash(request):
#     return render(request, 'Student_profiledash.html')


def Staff_studentsleave_table(request):
    if 'sfid' in request.session:
        if request.session.has_key('sfid'):
            sfid = request.session['sfid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=sfid)
        des = designation.objects.get(designation='student')
        sl = leave.objects.filter(designation_id=des.id).all().order_by('-id')
        return render(request, 'Staff_studentsleave_table.html',{'pro':pro,'sl': sl})
    else:
        return redirect('/')


def Staff_current_students(request):
    if 'sfid' in request.session:
        if request.session.has_key('sfid'):
            sfid = request.session['sfid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=sfid)
        des = designation.objects.get(designation='student')
        cs = user_registration.objects.filter(designation_id=des).filter(status='active') .all().order_by('-id')
        
        return render(request, 'Staff_current_students.html',{'pro':pro,'cs': cs,'des':des})
    else:
        return redirect('/')

def Staff_student_dashboard(request,id):
    if 'sfid' in request.session:
        if request.session.has_key('sfid'):
            sfid = request.session['sfid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=sfid)
        csd=user_registration.objects.filter(id=id)
        return render(request, 'Staff_student_dashboard.html',{'pro':pro,'csd':csd})
    else:
        return redirect('/')


def Staff_previous_students(request):
    if 'sfid' in request.session:
        if request.session.has_key('sfid'):
            sfid = request.session['sfid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=sfid)
        des = designation.objects.get(designation='student')
        ps = user_registration.objects.filter(designation_id=des).filter(status='resigned') .all().order_by('-id')
        return render(request, 'Staff_previous_students.html',{'pro':pro,'ps': ps,'des':des})
    else:
        return redirect('/')


def Staff_previous_student_dashboard(request,id):
    if 'sfid' in request.session:
        if request.session.has_key('sfid'):
            sfid = request.session['sfid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=sfid)
        psd=user_registration.objects.filter(id=id)
        return render(request, 'Staff_previous_student_dashboard.html',{'pro':pro,'psd':psd})
    else:
        return redirect('/')

def Acc_index(request):
    if 'accid' in request.session:
        if request.session.has_key('accid'):
            accid = request.session['accid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=accid)
        return render(request,'Acc_index.html',{'pro':pro})
    else:
        return redirect('/')

def Account_Student_det(request):
    if 'accid' in request.session:
        if request.session.has_key('accid'):
            accid = request.session['accid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=accid)
        return render(request, 'Account_Student_det.html',{'pro':pro})
    else:
        return redirect('/')

def Account_previous_students(request):
    if 'accid' in request.session:
        if request.session.has_key('accid'):
            accid = request.session['accid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=accid)
        des = designation.objects.get(designation='student')
        aps = user_registration.objects.filter(status ="resigned" or "Resigned", designation_id = des)
        pay = payment.objects.all()
        return render(request, 'Account_previous_students.html',{'pro':pro,'aps': aps,'pay':pay})
    else:
        return redirect('/')



def Staff_progress_report(request):
    if 'sfid' in request.session:
        if request.session.has_key('sfid'):
            sfid = request.session['sfid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=sfid)
        desi = designation.objects.get(designation='student')
        sps = user_registration.objects.filter(designation_id=desi).filter(status='active') .all().order_by('-id')
        return render(request, 'Staff_progress_report.html',{'pro':pro,'desi':desi,'sps': sps})
    else:
        return redirect('/')

def Staff_progress_report_add(request):
    if 'sfid' in request.session:
        if request.session.has_key('sfid'):
            sfid = request.session['sfid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=sfid)
        if request.method == 'POST':
            fn1 = request.POST['sname']
            fn2 = request.POST['ssubject']
            fn3 = request.POST['smark']
            fn4 = request.POST['sdate']
            
            
            students = user_registration.objects.get(fullname=fn1)
            
            new2 = progressreport(user=students, subject=fn2, mark=fn3, date=fn4)
            new2.save()
        return redirect('Staff_progress_report_show')
    else:
        return redirect('/')
    



def Staff_progress_report_show(request):
    if 'sfid' in request.session:
        if request.session.has_key('sfid'):
            sfid = request.session['sfid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=sfid)
        pr=progressreport.objects.all()
        desi = designation.objects.get(designation='student')
        sps = user_registration.objects.filter(designation_id=desi).filter(status='active') .all().order_by('-id')
    
        return render(request, 'Staff_progresss_report.html',{'pro':pro,'pr':pr,'sps':sps})
    else:
        return redirect('/')



def Staff_rejected_leave(request,id):
    if 'sfid' in request.session:
        if request.session.has_key('sfid'):
            sfid = request.session['sfid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=sfid)
        if request.method == 'POST':
            staff_reason=request.POST.get('reply')
            pro_sts = leave.objects.filter(id=id).update(leave_rejected_reason= staff_reason,status ='Rejected')
            
        
        return redirect('Staff_studentsleave_table')
    else:
        return redirect('/')


def Staff_accepted_leave(request,id):
    if 'sfid' in request.session:
        if request.session.has_key('sfid'):
            sfid = request.session['sfid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=sfid)
        al = leave.objects.filter(id=id).update(status ='Approved')  
        return redirect('Staff_studentsleave_table')
    else:
        return redirect('/')


def MAN_subjects(request):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)
        return render(request, 'MAN_subjects.html',{'pro':pro})
    else:
        return redirect('/')


def MAN_Viewsubject(request):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)
        sub=subject.objects.all()
        return render(request, 'MAN_Viewsubject.html',{'pro':pro,'sub':sub})
    else:
        return redirect('/')


def MAN_Updatesubject(request,id):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)
        sub=subject.objects.get(id=id)
        batches=batch.objects.all()
        return render(request, 'MAN_Updatesubject.html',{'pro':pro,'sub':sub,'batches':batches})
    else:
        return redirect('/')

def MAN_subjectupdate(request,id):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)   
        if request.method == 'POST':
            subed = subject.objects.get(id=id)
            subed.subject = request.POST.get('subj')
            subed.rate = request.POST.get('srate')
            
    
       
            try:
                subed.logo = request.FILES['slogo']
            except:
                pass
            
            br_id = request.POST.get("subbatch")
            subed.batch_id = br_id
            subed.save()
            return redirect('MAN_Viewsubject')
    else:
        return redirect('/')

def MAN_subject_delete(request, id):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)
        subed = subject.objects.get(id=id)   
        subed.delete()
        return redirect('MAN_Viewsubject')
    else:
        return redirect('/')