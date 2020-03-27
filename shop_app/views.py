from django.shortcuts import render
from .models import Items
# Create your views here.
def index(request):
    items = Items.objects.all()
    context = {'items':items}
    return render(request,'index.html',context)

def signin(request):
    return render(request,'signin.html')

def profile(request):
    return render(request,'profile.html')

def cart(request):
    return render(request,'cart.html')

def signup(request):
    return render(request,'signup.html')
