from django import forms  
from Mysite.models import User  
from Mysite.models import Regis
#USER FORM
class UserForm(forms.ModelForm):  

    class Meta:  
        model = User  
        fields = "__all__"  

#EMAIL SERVICE   
class Subscribe(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email
    
#REGISTER FORM
class RegisForm(forms.ModelForm):

    class Meta:
        model = Regis
        fields = "__all__"  
