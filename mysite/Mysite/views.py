from django.shortcuts import render, redirect  
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from Mysite.forms import UserForm 
from mysite.settings import EMAIL_HOST_USER
from Mysite.models import User
from django.views.generic import ListView, DetailView  
from reportlab.pdfgen import canvas  
from django.http import HttpResponse 
from . import forms
from Mysite.forms import Subscribe 
from django.core.mail import send_mail 
from Mysite.functions import handle_uploaded_file
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.  

#HOME PAGE
def index(request):
    return HttpResponse("Under Progress..")


#INSERT 
def usr(request):  
    if request.method == "POST":  
        form = UserForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = UserForm()  
    return render(request,'index.html',{'form':form})  

#SELECT 
def show(request):  
    users = User.objects.all()  
    page = request.GET.get('page', 1)

    paginator = Paginator(users, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request,"show.html",{'users':users})

#EDIT      
def edit(request, id):  
    user = User.objects.get(id=id)  
    return render(request,'edit.html', {'user':user})  

#UPDATE  
def update(request, id):  
    user = User.objects.get(id=id)  
    form = UserForm(request.POST, instance = user)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'user': user})  

#DELETE
def destroy(request, id):  
    user = User.objects.get(id=id)  
    user.delete()  
    return redirect("/show")
"""
#FILE UPLOAD
def ind(request):  
    if request.method == 'POST':  
        user = UserForm(request.POST, request.FILES)  
        if user.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        user = UserForm()  
    return render(request,"index.html",{'form':form})  
"""

""" 
#PDF GENRATOR
def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello, Javatpoint.")  
    p.showPage()  
    p.save()  
    return response  
"""

#SEND EMAIL
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Test Django Mail'
        message = 'Test Success...!!!'
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return redirect("/mail")
    return render(request, 'mail.html', {'form':sub})
