from django.db import models

class designation(models.Model):
    designation = models.CharField(max_length=100)


    # def _str_(self):
    #     return self.designation


class user_registration(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,null=True, blank=True)
   
    fullname = models.CharField(max_length=240, null=True)
    fathername = models.CharField(max_length=240, null=True)
    mothername = models.CharField(max_length=240, null=True)
    dateofbirth = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    gender = models.CharField(max_length=240, null=True)
    presentaddress1 = models.CharField(max_length=240, null=True)
    presentaddress2 = models.CharField(max_length=240, null=True)
    presentaddress3 = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    district = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    permanentaddress1 = models.CharField(max_length=240, null=True)
    permanentaddress2 = models.CharField(max_length=240, null=True)
    permanentaddress3 = models.CharField(max_length=240, null=True)
    permanentpincode = models.CharField(max_length=240, null=True)
    permanentdistrict = models.CharField(max_length=240, null=True)
    permanentstate = models.CharField(max_length=240, null=True)
    permanentcountry = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    alternativeno = models.CharField(max_length=240, null=True)
    employee_id = models.CharField(max_length=240,null=True,default='')
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    idproof = models.FileField(upload_to='images/', null=True, blank=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    attitude = models.IntegerField(default='0')
    creativity = models.IntegerField(default='0')
    workperformance = models.IntegerField(default='0')
    joiningdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    startdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')
 
    # def _str_(self):
    #     return self.fullname




class leave(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,null=True, blank=True)
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,null=True, blank=True)                        
    from_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    to_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    reason = models.TextField()
    leave_status = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    leaveapprovedstatus = models.CharField(max_length=200)
    leave_rejected_reason = models.CharField(max_length=300)

    
    # def _str_(self):
    #     return self.user

class progressreport(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,null=True, blank=True)
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,null=True, blank=True)                        
    date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    subject = models.CharField(max_length=200)
    mark = models.CharField(max_length=200)


class reported_issue(models.Model):
    reporter = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,
                                 related_name='reported_issuereporter', null=True, blank=True)
    reported_to = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,
                                    related_name='reported_issuereported_to', null=True, blank=True)
    issue = models.TextField()
    reported_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    reply = models.TextField()
    status = models.CharField(max_length=200)
    issuestatus = models.CharField(max_length=200)
    designation_id = models.CharField(max_length=200)


    def __str__(self):
        return self.reporter

class payment(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,null=True, blank=True)                        
    date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    payment = models.CharField(max_length=200)


class batch(models.Model):                        
    batch = models.CharField(max_length=200)


class subject(models.Model):
    batch = models.ForeignKey(batch, on_delete=models.CASCADE,null=True, blank=True)                        
    subject = models.CharField(max_length=200)
    rate = models.CharField(max_length=200)
    logo = models.FileField(upload_to='images/', null=True, blank=True)