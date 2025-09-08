from django.shortcuts import render,redirect
from django.http import HttpResponse
from products.models import Products
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .forms import ProductForm


# Create your views here.
def products_view(request,*args,**kwargs):
    product=Products.objects.all()
    context={
        "products":product
        
        }
    return render(request,"products.html",context)


def product_view(request,id=None):
    product = None
    if id is not None:
        product=Products.objects.get(id=id)
    
    return render(request,"details.html",{"product":product})

def search_view(request):
    query = request.GET.get("q")
    products = None
    if query is not None:
        products = Products.objects.filter(title__icontains=query)
    context={"products":products, "query": query}
    return render(request,'search.html',context)

@login_required
def create_view(request):
    form=ProductForm(request.POST or None)
    context={"form":form}
    if form.is_valid():
        obj=form.save()
        context['object']=obj
        context['created']=True

    return render(request,"create.html",context=context)