from django.shortcuts import render,HttpResponse,redirect

from django.contrib.auth.decorators import login_required

from .models import Blog

from .forms import createBlogForm

# Create your views here.
def blog_view(request):
    # return HttpResponse("Blog list")
    blogs=Blog.objects.all().order_by('publishedAt').reverse()
    print(blogs.order_by('publishedAt').reverse())
    return render(request,'blogs.html',{"blog":blogs})


def my_blogs_view(request):
    # return HttpResponse("Blog list")
    blogs=Blog.objects.filter(author_id=request.user.id)
    print(blogs)
    return render(request,'myblogs.html',{"blogs":blogs})


@login_required
def create_blog_view(request):
    form=createBlogForm(request.POST or None)
    context={"form":form}
    if form.is_valid():
        obj=form.save(commit=False)
        obj.author=request.user
        obj.save()
        context['obj']=obj
        context['created']=True
        return redirect("/blog")

    
    return render(request,'createblog.html',context)