from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return render(request,'login.html')
    print(request.user.get_full_name())
    context={
                'name':request.user.get_username()
            }
    return render(request,'index.html',context)
    
def loginUser(request):
    if request.method=='POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request,user)
            
            context={
                'name':user.get_username()
            }
            return render(request,'index.html',context)
        else:
            messages.error(request, 'Wrong Email or Password')

            
        

    return render(request,'login.html')
def logoutUser(request):
    logout(request)
    return render(request,'login.html')
