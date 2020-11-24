from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

#def login(request):
 #   form = AuthenticationForm(request.POST or None)
    #if request.method == 'POST':
        #if form.isValid():
    #    username = form.cleaned_data.get('username')
    #    raw_password = form.cleaned_dat.get('password1')
    #    user = authenticate(username = username, password = raw_password)
    #    return redirect('user profile')
    #else:
  #  return render(request, 'login.html', {'form': form})

def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.isValid():
            #form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_dat.get('password1')
            #user = authenticate(username = username, password = raw_password)
            user = form.save()
            login(request, user)
            return redirect('user profile')
    else:
        return render(request, 'signup.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'profile.html')
