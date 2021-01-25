from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def employee(request):
    users = User.objects.all()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            # to admin
            # new_user = User.objects.get(username=username)
            # new_user.is_staff = True
            # new_user.is_superuser = True
            # new_user.save()
            messages.success(request, f"{form.cleaned_data['username']} Successfully Added")
    else:
        form = UserCreationForm()
    context = {
        'users' : users,
        'form'  :   form,
    }
    return render(request, 'employee/employee.html', context)