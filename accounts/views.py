from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Users=Users.objects.all()




# Create your views here.
def login_view(request):
    context={"isLoggedin":request.user.is_authenticated}
    if(request.method=="POST"):
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('/')
        
    else:
        form=AuthenticationForm(request)  
    context["form"]=form
    return render(request,'login.html',context)

def register_view(request):

    form=UserCreationForm()
    context={"form":form}
    context["isLoggedIn"]=request.user.is_authenticated
    if request.method=="POST":

   
        form=UserCreationForm(request.POST or None)
        if form.is_valid():
            object=form.save()
            return redirect("/login")
    return render(request,"register.html",{"form":form})

@login_required
def logout_view(request):
    if(request.method=="POST"):        
        logout(request)
        return redirect('/')
    return render(request,'logout.html',{})


