from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from fyideliverapp.forms import UserForm, BusinessForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return redirect(business_home)

@login_required(login_url='/business/sign-in/')
def business_home(request):
    return render(request, 'business/home.html', {})

@login_required(login_url='/business/sign-in/')
def business_account(request):
    return render(request, 'business/account.html', {})

@login_required(login_url='/business/sign-in/')
def business_product(request):
    return render(request, 'business/product.html', {})

@login_required(login_url='/business/sign-in/')
def business_order(request):
    return render(request, 'business/order.html', {})

@login_required(login_url='/business/sign-in/')
def business_report(request):
    return render(request, 'business/report.html', {})

def business_sign_up(request):
    user_form = UserForm()
    business_form = BusinessForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        business_form = BusinessForm(request.POST, request.FILES)

        if user_form.is_valid() and business_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_business = business_form.save(commit=False)
            new_business.user =  new_user
            new_business.save()

            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))

            return redirect(business_home)

    return render(request, "business/sign_up.html", {
        "user_form": user_form,
        "business_form": business_form
    })
