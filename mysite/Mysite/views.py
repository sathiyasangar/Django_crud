from django.shortcuts import render, redirect  
from Mysite.forms import UserForm  
from Mysite.models import User
from django.views.generic import ListView, DetailView  
from reportlab.pdfgen import canvas  
from django.http import HttpResponse  
# Create your views here.  

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