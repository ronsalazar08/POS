from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import RegistrationForm

def employee(request):
    users = User.objects.all().order_by('-is_active', 'id')
    form = RegistrationForm()

    if request.method == "POST":
        form_ctrl = request.POST.get('form_ctrl')
        if form_ctrl == "new_emp":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f'<span class="text-primary">{form.cleaned_data["username"].upper()}</span> Successfully Added!')
                return redirect('employee')
        else:
            pk = form_ctrl
            form = RegistrationForm(request.POST, instance=User.objects.get(pk=pk))
            if form.is_valid():
                form.save()
                messages.success(request, f'<span class="text-primary">{form.cleaned_data["username"].upper()}</span> Successfully Edited!')
                return redirect('employee')
    context = {
        'users' : users,
        'form'  : form,
    }
    return render(request, 'employee/employee.html', context)


def delete_employee(request, pk):
    try:
        emp = User.objects.get(pk=pk)
        User.objects.get(pk=pk).delete()
        messages.success(request, f' <span class="text-primary">{emp.username.upper()}</span> Successfully Deleted!')
    except:
        messages.warning(request, f"Employee Don't exist!")
    
    return redirect('employee')