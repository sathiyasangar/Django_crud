from django import forms  
from Mysite.models import User  
from Mysite.models import Regis

class UserForm(forms.ModelForm):  

    class Meta:  
        model = User  
        fields = "__all__"  
        
class Subscribe(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email

class RegisForm(forms.ModelForm):

    class Meta:
        model = Regis
        fields = "__all__"