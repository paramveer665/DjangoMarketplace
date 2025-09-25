from django.urls import path,include

from .views import blog_view,create_blog_view,my_blogs_view

urlpatterns = [
    path('',blog_view,name="blogs"),
    path('create/',create_blog_view,name="createblog"),
    path('myblogs/',my_blogs_view,name='myblogs')
    
]
