from django.db import models

# Create your models here.
class User(models.Model):   
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    class Meta:  
        db_table = "user"  