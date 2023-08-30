from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *        
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, logout, authenticate
from datetime import datetime, timezone
from django.contrib.auth.decorators import login_required
from .models import Contribution, Loan, LoanFunding, Interest, Fee, LoanExpenditure,LoanFunding, LoanRepayment
from django.shortcuts import get_object_or_404


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)  # Set the password hash
            user.save()

            # Log in the user
            user = authenticate(phone_number=user.phone_number, password=password)
            if user:
                login(request, user)
                return redirect('home')  # Redirect to the homepage or any other page after successful registration
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})  # Pass the form to the template


def home(request):
    return render(request, 'home.html')


def login_user(request):
    phone_number = request.POST.get("phone_number")
    password = request.POST.get("password")
    user = authenticate(request, phone_number=phone_number, password=password)
    print(user)
    if user is not None:
        print(f"User in role {user.role}")
        login(request, user)
        return redirect("dashboard")

    return render(request, "login.html")


def logout(request):
    logout(request)
    return redirect("login")

def join_group(request):
    groups = CreateGroup.objects.all()
    return render(request, 'join_group.html',{'groups':groups}) 

def create_group(request):
    form = CreateGroupForm()
    if request.method == "POST":
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_group')
    context = {
        'form':form,
    }
    return render(request, 'create_group.html',context) 


def view_groups(request,id):
    queryset = CreateGroup.objects.get(id=id)
    group_name=queryset.group_name
    records = Member.objects.filter(group_id=id)
    context = {'group_name':group_name,'records':records}
    return render(request,'view_groups.html',context)

def proceed(request):
    # groups = CreateGroup.objects.all()
    return render(request, 'proceed.html') 

def member_contribution(request):
    form = ContributionForm()
    if request.method == "POST":
        form = ContributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_member_contribution')
    context = {
        'form':form,
    }
    return render(request, 'member_contribution.html',context) 

def view_member_contribution(request):
    contributions = Contribution.objects.all()
    context = {
        'contributions':contributions,
    }
    return render (request, 'view_contribution.html',context)


def fund_loan(request):
    if request.method == "POST":
        form = LoanFundingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fund_loan_add')
    else:
        form = LoanFundingForm()

    context = {
        'form': form,
    }
    return render(request, 'fund_loan.html', context)


def fund_loan_add(request):
    funders = LoanFunding.objects.all()
    context = {
        'funders': funders,
    }
    return render(request, 'fund_loan_add.html', context)


def borrow_loan(request):
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrow_loan_add')
    else:
        form = LoanForm()

    context = {
        'form': form,
    }
    return render(request, 'borrow_loan.html', context)


def borrow_loan_add(request):
    funders = Loan.objects.all()
    context = {
        'funders': funders,
    }
    return render(request, 'borrow_loan_add.html', context)


def repay_loan(request):
    if request.method == "POST":
        form = LoanRepaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repay_loan_add')
    else:
        form = LoanRepaymentForm()

    context = {
        'form': form,
    }
    return render(request, 'repay_loan.html', context)


def repay_loan_add(request):
    funders = LoanRepayment.objects.all()
    context = {
        'funders': funders,
    }
    return render(request, 'repay_loan_add.html', context)


def group_set_up(request):
     
    if request.method == "POST":
         form = MemberForm(request.POST)
         if form.is_valid():
             form.save()
    else:
        form = MemberForm()
    return render(request, 'group_set_up.html',{'form':form}) 


def add_member(request):
    group_form = CreateGroupForm()

    if request.method == 'POST':
        group_form=CreateGroupForm(request.POST)
        if group_form.is_valid():
                group_form.save()
        form = MemberForm(request.POST)
        if form.is_valid():
           
            form.save()  # Save the validated form data to the database
            return redirect('view_member')  # Redirect to the view_member page after saving
    else:
        form = MemberForm()
    
    return render(request, 'add_member.html', {'form': form})


def view_member(request):
    members=Member.objects.all()
    context = {
        "members":members
    }
    return render (request,"view_member.html",context)

def create_group(request):
    records = CreateGroup.objects.all()

    if request.method == "POST":
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            new_group = form.save()
            return redirect("join_group", id=new_group.id)  # Redirect to 'join_group' with group ID
        else:
            print(form.errors)
    else:
        form = CreateGroupForm()

    context = {"form": form, "records": records, "create_group": "active"}
    return render(request, "create_group.html", context)



 

