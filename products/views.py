from django.shortcuts import render,redirect
from django.http import HttpResponse
from products.models import Products
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

product=Products.objects.all()


# Create your views here.
def products_view(request,*args,**kwargs):
    context={
        "products":product
        
        }
   
    
            
            
           
    return render(request,"products.html",context)


def product_view(request,id=None):
    if id is not None:
        obj=Products.objects.get(id=id)
    
    return render(request,"details.html",{"context":obj})

def search_view(request):
    
    result=request.GET.get("q")
    
    search_object=None
    if result is not None:
        search_object=Products.objects.get(id=result)   
   


    context={"res":search_object}
   
    return render(request,'search.html',context)

@login_required
def create_view(request):
    form=ProductForm()
    context={"form":form}    
    
    form=ProductForm(request.POST or None)
    context["form"]=form
    if form.is_valid():
        new_object=form.save()
            # title=form.cleaned_data.get("title")
            # desc=form.cleaned_data.get("desc")
            # price=form.cleaned_data.POST.get("price")
            # featured=True if request.POST.get("featured")=='on' else False
            # active=True if request.POST.get("active")=='on' else False
            # new_object=Products.objects.create(title=title,price=price,desc=desc,active=active,featured=featured)
        context['object']=new_object
        context['created']=True

    return render(request,"create.html",context=context)