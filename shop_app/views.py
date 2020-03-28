from django.shortcuts import render,redirect
from .models import Items
from django.contrib.auth.models import User,auth
from .models import Profile
# Create your views here.
def index(request):
    items = Items.objects.all()
    context = {'items':items}
    return render(request,'index.html',context)

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['fname']
        
        lastname = request.POST['lname']
        username = request.POST['uname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password1)
        user.save()
        return redirect("/")
    else:

        return render(request,'signup.html')

def profile(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request,'profile.html',context)

def cart(request):
    return render(request,'cart.html')

def signin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']

        user = auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            print("Not valid")
            return redirect("signin")
        
    else:
        return render(request,'signin.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

