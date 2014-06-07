from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.views import login as auth_login

def login(request):
    if not request.user.is_authenticated():
        return auth_login(request)
    else:
        return HttpResponseRedirect("/accounts/profile/")

def register(request):
    if request.user.is_authenticated():
        return render(request, "registration/register_logged.html")

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/accounts/register/done")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

def register_done(request):
    if request.user.is_authenticated():
        return render(request, "registration/register_logged.html")

    return render(request, "registration/register_done.html")
