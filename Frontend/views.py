from django.shortcuts import render, redirect
from django.contrib import messages
from Backend.models import VehicleDB, Vehicle_Category, Admindb, Contactdatab
from Frontend.models import CustomerDetails
from datetime import datetime, timedelta



# Create your views here.
def home_page(request):
    data = Vehicle_Category.objects.all()
    dealer = Admindb.objects.all()
    return render(request, 'home_page.html', {'data': data, 'dealer': dealer})


def contacts_page(request):
    data = Vehicle_Category.objects.all()
    dealer = Admindb.objects.all()
    return render(request, 'contacts_page.html', {'data': data, 'dealer': dealer})


def contactdatabase(request):
    if request.method == 'POST':
        na = request.POST.get('name')
        em = request.POST.get('email')
        sb = request.POST.get('subject')
        mg = request.POST.get('message')
        obj = Contactdatab(Name=na, EmailID=em, Subject=sb, Message=mg)
        obj.save()
        return redirect(contacts_page)


def discategory(request, itemCatg):
    print("===itemCatg===", itemCatg)
    catg = itemCatg.upper()
    data = Vehicle_Category.objects.all()
    dealer = Admindb.objects.all()
    products = VehicleDB.objects.filter(Cname=itemCatg)
    context = {
        'products': products,
        'catg': catg,
        'data': data,
        'dealer': dealer

    }
    return render(request, 'category_page.html', context)


def display_dealers(request, dealname):
    data = Vehicle_Category.objects.all()
    dealer = Admindb.objects.filter(Name=dealname)
    return render(request, 'dealers_page.html', {'data': data, 'dealer': dealer})


def vehicle_show(request, dataid):
    cate = Vehicle_Category.objects.all()
    data = VehicleDB.objects.get(id=dataid)
    dealer = Admindb.objects.all()
    return render(request, 'vehicles.html', {'data': data, 'cate': cate, 'dealer': dealer})


def login_page(request):
    return render(request, 'login_page.html')

def congratulation_page(request):
    return render(request, 'congratulation.html')


def register_page(request):
    return render(request, 'register.html')
def payment_page(request,dataid):
    data = VehicleDB.objects.get(id=dataid)
    return render(request, 'payment_page.html',{'data': data})


def customersave(request):
    if request.method == "POST":
        un = request.POST.get('username')
        em = request.POST.get('email')
        pw = request.POST.get('password')
        cp = request.POST.get('confirmpassword')
        if pw == cp:
            obj = CustomerDetails(username=un, email=em, password=pw, confirmpassword=cp)
            obj.save()
            messages.success(request,"User Register Successfully")
            return redirect(login_page)
        else:
            messages.warning(request,"Sorry.... Invalid Username Or Password")
            return redirect(register_page)
    return render(request, 'register.html', {'msg': "sorry.... password not matched"})


def customerlogin(request):
    if request.method == 'POST':
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if CustomerDetails.objects.filter(username=username_r, password=password_r).exists():
            request.session['username'] = username_r
            request.session['password'] = password_r
            messages.success(request,"User Login successfully")

            return redirect(home_page)
        else:
            messages.warning(request,"Sorry.... Invalid Username Or Password")

            return render(request, 'login_page.html', {'msg': "sorry.... invalid username or password"})


def customerlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(home_page)

#
# def sort_by(request):
#     now = datetime.now()
#     start_time = now - timedelta(hours=24)
#     print(start_time,"kkkkkkkkkkkkkkkk")
#     recent_data = VehicleDB.objects.filter(created__gte=start_time)
#     print(recent_data,"llllllllllllllllllllllll")
#     return render(request, 'category_page.html', {'recent_data': recent_data})

