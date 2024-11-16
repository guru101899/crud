from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User
from django.contrib.auth.hashers import make_password


# Create your views here.

def add(request):
    stu=User.objects.all()
    if request.method == 'POST':
        fm=UserForm(request.POST)
        if fm.is_valid():
            user=fm.save(commit=False)
            user.password = make_password(user.password) 
            user.save()
            fm=UserForm()
    else:
        fm=UserForm()
     
    return render(request,'add.html',{'form':fm,'stu':stu})


def update(request, id):
    pi = User.objects.get(pk=id)  
    if request.method == "POST":
        fm = UserForm(request.POST, instance=pi) 

        if fm.is_valid():
            user = fm.save(commit=False)  
            user.password = make_password(user.password)  
            user.save() 
            return redirect('/')  
    else:
        fm = UserForm(instance=pi)  
    
    return render(request, 'update.html', {'form': fm})


def delete(request,id):
    if request.method == 'POST':
        gt=User.objects.get(pk=id)
        gt.delete()
        return redirect ('/')