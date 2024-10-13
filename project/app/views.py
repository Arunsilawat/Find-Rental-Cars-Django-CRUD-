from django.shortcuts import render
from.models import Userdata
from.models import Book_data
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
    if request.method=='POST':
        email=request.POST.get('email')
        password1=request.POST.get('password')
        user=Userdata.objects.filter(email=email)
        if user:
            admindata=Userdata.objects.get(email=email)
            fname=admindata.fname
            lname=admindata.lname
            email=admindata.email
            password=admindata.password
            if password==password1:
                user={
                    'fnm':fname,
                    'lnm':lname,
                    'em':email,
                    'pass':password
                }
                return render(request,'select.html',{'user':user})
            else:
                msg="Password Not Matched"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="Email Id Not Registered"
            return render(request,'login.html',{'msg':msg})
    return render(request,'login.html')
def logout(request):
    return render(request,'home.html')
def carinfo(request):
    if request.method=='POST':
        carnm=request.POST.get('carnm')
        carpay=request.POST.get('carpay')
        fnm=request.POST.get('fnm')
        lnm=request.POST.get('lnm')
        em=request.POST.get('em')
        data={
            'cnm':carnm,
            'cpay':carpay,
            'fnm':fnm,
            'lnm':lnm,
            'em':em,
        }
        return render(request,'carinfo.html',{'data':data})
def datadisplay(request):
    if request.method=='POST':
        fname=request.POST.get('fnm')
        lname=request.POST.get('lnm')
        email=request.POST.get('em')
        carnm=request.POST.get('cnm')
        amount=request.POST.get('cpay')
        address=request.POST.get('add')
        pick=request.POST.get('pdate')
        drop=request.POST.get('ddate')
        feedback=request.POST.get('feed')
        Book_data.objects.create(fname=fname,lname=lname,email=email,carnm=carnm,amount=amount,address=address,pick=pick,drop=drop,feedback=feedback)
        data=Book_data.objects.filter(email=email).values()
        return render(request,'datadisplay.html',{'data':data})
def delete(request,pk,em):
    user=Book_data.objects.filter(id=pk)
    if user:
        user=Book_data.objects.get(id=pk)
        email=user.email
        user.delete()
        data=Book_data.objects.filter(email=email)
        return render(request,'datadisplay.html',{'data':data})
    else:
        data=Book_data.objects.filter(email=em)
        return render(request,'datadisplay.html',{'data':data})
 