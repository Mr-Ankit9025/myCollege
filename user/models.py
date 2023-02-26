from django.db import models

# create your models here.
class contactInfo(models.Model):
    Name=models.CharField(max_length=80)
    Email=models.CharField(max_length=30)
    Mobile=models.CharField(max_length=30)
    Msg=models.TextField()

    def _str_(self):
        return self.Name

############### u gallery models#########################
class ugallery(models.Model):
    gdes=models.CharField(max_length=200)
    picture=models.ImageField(upload_to='static/gallery/',default="")

    ################## my college sign in###################
class sturegister(models.Model):
    rno=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    year=models.CharField(max_length=40)
    smobile=models.CharField(max_length=50)
    gmobile=models.CharField(max_length=50)
    pic=models.ImageField(upload_to='static/profile/',null=True)
    rdate=models.CharField(max_length=100)


class city(models.Model):
    cname=models.CharField(max_length=30)
    cdate=models.DateField()

class company(models.Model):
    cname=models.CharField(max_length=200)
    clogo=models.ImageField(upload_to='static/company')
    def _str_(self):
        return self.cname

class stuplacement(models.Model):
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    stupic=models.ImageField(upload_to='static/profile',null=True)
    designation=models.CharField(max_length=70)
    syear=models.CharField(max_length=40)
    cpic=models.ImageField(upload_to='static/company')
    rdate=models.DateField()
    cname=models.ForeignKey(company,on_delete=models.CASCADE,null=True)
    pcity=models.CharField(max_length=60)

##############gallery#########################
class vgallery(models.Model):
    vlink=models.TextField()
    vdes=models.TextField()
    vtitle=models.CharField(max_length=200)
    vdate=models.DateField()

###################################################
class mycourse(models.Model):
    cname=models.CharField(max_length=50)
    branch=models.CharField(max_length=30)
    seats=models.CharField(max_length=50)
    hod=models.CharField(max_length=50)
    duration=models.CharField(max_length=50)
    cpic=models.ImageField(upload_to='static/course',null=True)
    sdate=models.CharField(max_length=100)
    eligibilty=models.CharField(max_length=50)
    fee=models.CharField(max_length=200)
    hodpic=models.ImageField(upload_to='static/hod',null=True)

###########################################
class infrastructure(models.Model):
    iname=models.CharField(max_length=30)
    ipic=models.ImageField(upload_to='static/infra',null=True)


#######################################################

class teacher(models.Model):
    tname=models.CharField(max_length=50)
    tbranch=models.CharField(max_length=50)
    tpic=models.ImageField(upload_to='static/faculty',null=True)


