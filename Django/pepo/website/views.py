from django.shortcuts import render
# from .models import Member
# from .forms import Memberform
# from Django.pepo.website.models import Member
# Create your views here.
def index(request):
    return render(request,'index.html',{})

def login(request):
    # if request.method =="POST":
    #     form= Memberform(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #     return render(request,'join.html',{})
    # else:
    return render(request, 'login.html',{})

	

def period_tracker(request):
    return render(request,'period_tracker.html',{})

def products(request):
    return render(request,'products.html',{})    

def blog(request):
    return render(request,'blog.html',{})    