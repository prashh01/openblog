from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.models import User
from django.forms import widgets,ImageField
from .models import Post, Report
from django.utils.translation import gettext,gettext_lazy as _

class Signup(UserCreationForm):
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email']
        labels = {'first_name':'First Name', 'last_name':'Last Name', 'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                   'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'}),
                   
        }
       
class Login(AuthenticationForm):
    username= UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password= forms.CharField(label =_("Password") , strip=False, 
                              widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ['title', 'desc','photo']
        labels = {'title':'Title', 'desc':'Description','photo':'Photo'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'}),
        }
        
        
class ReportForm(forms.ModelForm):
    class Meta:
        model= Report
        fields= ['name', 'email','username','message']
        labels = {'name':'Name', 'email':'Eamil','username':'Username','message':'Message'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'}),
        }
        