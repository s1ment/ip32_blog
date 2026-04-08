from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def add_user(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            return redirect('/users/')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})