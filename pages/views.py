from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello Django</h1>")
    return render(request,"home.html",{})
def about_view(*args,**kwargs):
    return HttpResponse("<h1>This is about page</h1><h2>We are new to this</h2>")



