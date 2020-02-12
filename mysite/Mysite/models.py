from django.db import models

# Create your models here.
class User(models.Model):   
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    #efiles = models.FileField() 
    #epassword = models.CharField(max_length=255, blank=True)

    class Meta:     
        db_table = "user"    

    
class Regis(models.Model):  
    rid = models.AutoField(primary_key=True)  
    rname = models.CharField(max_length=200, null=False)  
    remail = models.EmailField()  
    rpass = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:  
        db_table = "register"   