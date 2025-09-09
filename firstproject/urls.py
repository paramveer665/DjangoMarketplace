"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view,about_view
from products.views import products_view,product_view,search_view,create_view

from accounts.views import login_view,logout_view,register_view

urlpatterns = [
    path('',home_view,name='home'),
    path('admin/', admin.site.urls),
    path('about/',about_view,name="about"),
    path('create/',create_view,name="create"),
    path('home/',home_view),
    path('login/',login_view,name="login"),
    path('logout/',logout_view),    
    path('products',products_view),
    path('search/',search_view),    
    path('product/<int:id>/',product_view),
    path('register/',register_view)
   
    
]