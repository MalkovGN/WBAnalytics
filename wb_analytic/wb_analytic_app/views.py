from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from .services import collect_page_info, collect_product_info
from .models import ProductInfo


def home(request):
    return render(request, 'wb_analytic_app/home_page.html')


def login_user(request):
    """
    Authentication function
    """
    if request.method == 'GET':
        return render(request, 'wb_analytic_app/login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return (
                request,
                'wb_analytic_app/login.html',
                {'form': AuthenticationForm, 'error': 'Username or password didnt match'}
            )
        else:
            login(request, user)
            return redirect('current_user')


@login_required
def logout_user(request):
    """
    Logout function
    """
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def current_user(request):
    """
    The first page after
    registration/authentication
    """
    if request.method == 'GET':
        return render(request, 'wb_analytic_app/current_user.html')
    else:
        collect_page_info()
        # collect_product_info()
        return render(request, 'wb_analytic_app/current_user.html')

    # return render(request, 'wb_tracker_app/currentuser.html', {'cards': cards})


def check_null_objects(request):
    null_objects = ProductInfo.objects.filter(sold_number__isnull=True)
    if request.method == 'GET':
        return render(request, 'wb_analytic_app/current_user.html', {'obj': null_objects})
