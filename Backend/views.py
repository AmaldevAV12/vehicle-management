from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from Backend.models import Vehicle_Category, VehicleDB, Admindb,Contactdatab


# Create your views here.
def indexpage(request):
    return render(request, 'indexpage.html')



# Category
def vehicles_category(request):
    return render(request, 'vehicles_category.html')


def vehicles_category_form(request):
    if request.method == "POST":
        na = request.POST.get('cname')
        # col = request.POST.get('brand')
        com = request.POST.get('comments')
        img = request.FILES['image']
        obj = Vehicle_Category(Cname=na, Comments=com, Image=img)
        obj.save()
        return redirect(vehicles_category)


def display_vehicles_category(request):
    data = Vehicle_Category.objects.all()
    return render(request, 'display_vehicles_category.html', {'data': data})


def edit_vehicles_category(request, dataid):
    data = Vehicle_Category.objects.get(id=dataid)
    return render(request, 'edit_vehicles_category.html', {'data': data})


def update_vehicles_category(request, dataid):
    if request.method == "POST":
        na = request.POST.get('cname')
        # br = request.POST.get('brand')
        com = request.POST.get('comments')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Vehicle_Category.objects.get(id=dataid).Image
        Vehicle_Category.objects.filter(id=dataid).update(Cname=na,  Comments=com, Image=file)
        return redirect(display_vehicles_category)


def delete_vehicles_category(request, dataid):
    data = Vehicle_Category.objects.filter(id=dataid)
    data.delete()
    return redirect(display_vehicles_category)


# Vehicles
def add_vehicles(request):
    data = Vehicle_Category.objects.all()
    return render(request, 'add_vehicles.html', {'data': data})


def vehicles(request):
    if request.method == 'POST':
        cn = request.POST.get('category')
        vn = request.POST.get('vname')
        col = request.POST.get('colour')
        pr = request.POST.get('price')
        com = request.POST.get('comments')
        img = request.FILES['image']
        obj = VehicleDB(Cname=cn, Vname=vn, Colour=col, Price=pr, Comments=com, Image=img)
        obj.save()
        return redirect(add_vehicles)


def display_vehicles(request):
    data = VehicleDB.objects.all()
    return render(request, 'display_vehicles.html', {'data': data})


def edit_vehicles(request, dataid):
    data = VehicleDB.objects.get(id=dataid)
    da = Vehicle_Category.objects.all()
    return render(request, 'edit_vehicles.html', {'data': data,'da':da})


def update_vehicles(request, dataid):
    if request.method == "POST":
        cn = request.POST.get('category')
        vn = request.POST.get('vname')
        col = request.POST.get('colour')
        pr = request.POST.get('price')
        com = request.POST.get('comments')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = VehicleDB.objects.get(id=dataid).Image
        VehicleDB.objects.filter(id=dataid).update(Cname=cn, Vname=vn, Colour=col, Price=pr, Comments=com, Image=file)
        return redirect(display_vehicles)


def delete_vehicles(request, dataid):
    data = VehicleDB.objects.filter(id=dataid)
    data.delete()
    return redirect(display_vehicles)
#contact us
def display_contacts(request):
    data = Contactdatab.objects.all()
    return render(request, 'display_contacts.html', {'data': data})

def delete_contacts(request, dataid):
    data = Contactdatab.objects.filter(id=dataid)
    data.delete()
    return redirect(display_contacts)

#Admin

def adminpage(request):
    return render(request,'admin.html')

def adminpagedb(request):
    if request.method == "POST":
        na = request.POST.get('name')
        mb = request.POST.get('mob')
        em = request.POST.get('mail')
        img = request.FILES['image']
        re = request.POST.get('review')
        # pd = request.POST.get('pwd')
        # cp = request.POST.get('confpwd')
        obj =Admindb(Name=na,MobileNumber=mb,EmailID=em,Image=img,Review=re)
        obj.save()
        return redirect(adminpage)

def displayadminpg(requset):
    data = Admindb.objects.all()
    return render(requset,'display_admin.html',{'data':data})

def editadmin(request,dataid):
    data = Admindb.objects.get(id=dataid)
    return render(request, 'edit_admin.html', {'data': data})

def updateadminpage(request,dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        mb = request.POST.get('mob')
        em = request.POST.get('mail')
        re = request.POST.get('review')
        # pd = request.POST.get('pwd')
        # cp = request.POST.get('confpwd')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = Admindb.objects.get(id=dataid).Image
            Admindb.objects.filter(id=dataid).update(Name=na,MobileNumber=mb,EmailID=em, Image=file,Review=re)
            return redirect(displayadminpg)

def deleteadmin(request,dataid):
    data = Admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadminpg)
#
def logindata(request):
    return render(request,'login.html')

def logindb_fun(request):
    if request.method == "POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=pwd)
            if user is not None:
                login(request, user)
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(indexpage)

            else:
                return redirect(logindata)
        else:
            return redirect(logindata)

def customerlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(logindata)