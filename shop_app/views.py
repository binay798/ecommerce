from django.shortcuts import render,redirect
from .models import Items
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
    items = Items.objects.all()
    context = {'items':items}
    return render(request,'index.html',context)

def signin(request):
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

        return render(request,'signin.html')

def profile(request):
    return render(request,'profile.html')

def cart(request):
    return render(request,'cart.html')

def signup(request):
    return render(request,'signup.html')
