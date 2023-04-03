from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from . models import *
from django.http import HttpResponse
from .decorators import *
@role_based
def index(request):
    return render(request, 'ipdc/index.html')
def investor_personal_information(request):
    return render(request, 'ipdc/Investor_dashboard/investor_personal_information.html')

def investor_project_information(request):
    return render(request, 'ipdc/Investor_dashboard/investor_project_information.html')

def investor_file_information(request):
    return render(request, 'ipdc/Investor_dashboard/investor_file_information.html')

def park_admin_dashboard(request):
    return render(request, 'ipdc/Park_admin_dashboard/index3.html')

def manager_dashboard(request):
    return render(request, 'ipdc/manager_dashboard/index2.html')

def board_dashboard(request):
    return render(request, 'ipdc/Board_dashboard/index2.html')

def oiib_dashboard(request):
    return render(request, 'ipdc/OIIB_Dashboard/index4.html')


@login_required(login_url='login')
def profilepage(request):
    investorform=InvestorForm()
    if request.method =="POST":
        investorform=InvestorForm(request.POST)
        print(investorform)
        if investorform.is_valid():
            investor=investorform.save(commit=False)
            investor.user = request.user
            investor.save()

            return HttpResponse('added')
    context = {'investorform':investorform}
    return render(request, 'ipdc/investorform.html',context)

@login_required(login_url='login')
def landpage(request):
    landform=LandForm()
    if request.method =='POST':
        landform=LandForm(request.POST)
        if landform.is_valid():
            land=landform.save(commit=False)
            invest=Investor.objects.get(user=request.user)
            land.investor = invest
            land.save()
            return HttpResponse("done")
    context={'landform':landform}
    return render(request,'ipdc/investorform2.html',context)
@login_required(login_url='login')
def filesubmission(request):
    fileform=FileForm()
    if request.method =='POST':
        fileform=FileForm(request.POST,request.FILES)
        if fileform.is_valid():
            filef=fileform.save(commit=False)
            invest=Investor.objects.get(user=request.user)
            filef.investor = invest
            filef.save()
            return HttpResponse("it is gone")
    context={'fileform':fileform}
    return render(request,'ipdc/investorform3.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        print("working")
        email = request.POST.get('email')
        password =request.POST.get('password')
        try:
            uuser=User.objects.get(email=email)
        except:
            return HttpResponse("Invalid")
        user = authenticate(request, username=uuser.username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'ipdc/login.html', context)

def logoutpage(request):
    logout(request)
    return redirect('login')
