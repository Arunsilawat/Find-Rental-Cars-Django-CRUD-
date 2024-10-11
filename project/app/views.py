from django.shortcuts import render
from.models import Userdata
# Create your views here.
def home(request):
    return render(request,'home.html')
def select(request):
    return render(request,'select.html')
def register(request):
    if request.method=='POST':
        fname=request.POST.get('firstName')
        lname=request.POST.get('lastName')
        email=request.POST.get('email')
        password=request.POST.get('password')
        use=Userdata.objects.filter(email=email)
        if use:
            msg="Email Id Already Exist"
            return render(request,'home.html',{'msg':msg})
        else:
            msg="Registration Successfull"
            Userdata.objects.create(fname=fname,lname=lname,email=email,password=password)
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'home.html')
def login(request):
    # if request.method=='POST':
    return render(request,'login.html')