from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from .models import *
from django.db.models import F
import os

def home(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def addregister(request):
    if request.method=="POST":
        a=request.POST.get('name') 
        b=request.POST.get('email')
        c=request.POST.get('password')
        d=request.POST.get('phone')   
        ins=regtable(name=a,email=b,password=c,phone=d)
        ins.save()
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def addlogin(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    if email=='admin@gmail.com'and password=='admin':
       request.session['admin@gmail.com']='admin@gmail.com'
       request.session['admin']='admin'
       ins=regtable.objects.all()
       return render(request,'index.html')

    elif regtable.objects.filter(email=email,password=password).exists():
        userdetails=regtable.objects.get(email=email,password=password)
        if userdetails.email==request.POST['email']:
            request.session['userid']=userdetails.id
            request.session['username']=userdetails.name 
            return render(request,'index.html')  
    else:
         return render(request,'login.html')
def logout(request):
    session_keys=list(request.session.keys())   
    for key in session_keys:
            del request.session[key] 
    return redirect(index)
def viewuser(request):
    user=regtable.objects.all()
    return render(request,'viewuser.html',{'result':user}) 

def upload(request):
    return render(request,'upload.html')

'''def addupload(request):
    if request.method == "POST":
        myfile=request.FILES['file'] 
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        try:
            os.remove(os.path.join(settings.MEDIA_ROOT,'input/test/test.csv'))
        except:
            pass
        fs=FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT,'input/test/'))  
        fs.save("test.csv", myfile) 
        fs=FileSystemStorage()
        fs.save(myfile.name,myfile) 
        #k.clear_session()

        result=test1.predict()
        ins=uploadtable(images=filename,user_id=request.session['userid'],result=result)
        ins.save()
    return render(request,'upload.html',{'result':result})'''



def addupload(request):
    if request.method=="POST":
        u_id = request.session['userid']
        result = request.POST.get('result')
        image = request.FILES['image']
        try:
            os.remove("media/input/test.mp4")
        except:
            pass
        fs = FileSystemStorage(location="media/input")
        fs.save("test.mp4",image)
        #os.system("C:\\virtualenv\\scratch_env\\Scripts\\python.exe yolov5/detect.py --source media/input/test.mp4 --weights yolov5/yolov5s.pt")
        os.system("python yolo\\detect.py --img 640 --conf 0.25 --weights yolo\\best.pt --source media\\input\\test.mp4 --view-img")
        fs = FileSystemStorage()
        fs.save("test.mp4",image)
        ins=uploadtable(images=image,user_id=request.session['userid'],result=result)
        ins.save()
        return render(request,'index.html')
    


def viewupload(request):
    user=uploadtable.objects.all()
    return render(request,'viewupload.html',{'result':user}) 
