"""
mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Mysite import views 

urlpatterns = [
    path('', views.logg, name='index'),
    path('admin/', admin.site.urls),
    path('usr', views.usr),  
    path('show',views.show),   
    path('mail',views.subscribe),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy), 
    #path('reg',views.reg),
    path('regs',views.regins),
    
    #path('ind',views.ind),  
    #path('pdf',views.getpdf), 
]
