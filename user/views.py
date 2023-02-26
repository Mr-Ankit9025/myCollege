from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'user/index.html')
def home(request):
    return render(request,'user/index.html')
def aboutus(request):
    return render(request,'user/aboutus.html')

def courses(request):
    c=mycourse.objects.all().order_by('-id')
    if request.method=="GET":
        x=request.GET.get('search')
        if x is not None:
            c=mycourse.objects.all().filter(Q(cname__icontains=x) | Q(branch__icontains=x) | Q(hod__icontains=x)| Q(seats__icontains=x))



    md={"cdata":c}



    return render(request,'user/courses.html',md)
def register(request):
    s=False
    if request.method == "POST":
        Name = request.POST.get('name')
        RNo = request.POST.get('rno')
        course = request.POST.get('course')
        year = request.POST.get('year')
        date = request.POST.get('rdate')
        Email = request.POST.get('email')
        mobile = request.POST.get('mob')
        gmob = request.POST.get('gmob')
        picture = request.POST.get('propic')
        sturegister(name=Name, rno=RNo, course=course, year=year, rdate=date, email=Email, smobile=mobile, gmobile=gmob,
                    pic=picture).save()
    s=True
    mydict = {"status":s}
    return render(request,'user/register.html',context=mydict)
def contactus(request):
    s=False
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mob')
        d=request.POST.get('msg')
        contactInfo(Name=a,Email=b,Mobile=c,Msg=d).save()
        s=True


    return render(request,'user/contactus.html',context={"msg":s})
def login(request):
    return render(request,'user/login.html')


def infra(request):
    data=infrastructure.objects.all().order_by('-id')
    mydict={"idata":data}
    return render(request,'user/infra.html',mydict)

def facualty(request):
    data = teacher.objects.all().order_by('-id')
    mydict = {'fdata':data}
    return render(request,'user/facualty.html',mydict)



def gallery(request):
    x=ugallery.objects.all()
    mydict={"data":x}

    return render(request,'user/gallery.html',context=mydict)

def placement (request):
    p=stuplacement.objects.all().order_by('-id')
    if request.method=="GET":
        x=request.GET.get('search')
        if x is not None:
            p=stuplacement.objects.all().filter(Q(name__icontains=x) | Q(course__icontains=x) | Q(designation__icontains=x)| Q(syear__icontains=x))
    md={"pdata":p}
    return render(request,'user/placement.html',md)


def vdogallery(request):
    data=vgallery.objects.all().order_by('-id')
    myd={"vdata":data}
    return render(request,'user/video.html',myd)
def vdodetails(request):
    y=request.GET.get('id')
    x=vgallery.objects.all().filter(id=y)
    myd={"vdata":x}
    return render(request,'user/details.html',myd)