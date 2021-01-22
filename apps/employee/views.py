from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register_employee(request):
    form = UserCreationForm()
    context = {
        'form'  :   form,
    }
    return render(request, 'employee/register_employee.html', context)