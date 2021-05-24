from django.contrib.auth import authenticate
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import Signup, Login, PostForm, ReportForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as django_logout
from .models import Post, Report
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request, 'blog/home.html', context)



def dashboard(request):
    if request.user.is_authenticated:  
        posts =Post.objects.all() 
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        context={'posts':posts,'full_name':full_name,'groups':gps} 
        return render(request, 'blog/dashboard.html', context)
    else:
        HttpResponseRedirect('/login/')

def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    form=Signup()
    if request.method=='POST':
        form=Signup(request.POST)
        if form.is_valid():
            user=form.save()
            group= Group.objects.get(name="Author")
            user.groups.add(group)
    else:
        form=Signup()
    
    
    context={'form':form}
    return render(request, 'blog/signup.html',context)

def login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=Login(request=request, data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user= authenticate(username=uname, password=upass)
                if user is not None:
                    auth_login(request,user)
                    messages.success(request, 'Logged in Successfully!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form=Login()
        context={'form':form}
        return render(request,'blog/login.html',context)
    else:
        return HttpResponseRedirect('/dashboard/')


def add(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PostForm(request.POST, request.FILES )
            if form.is_valid():
                title=form.cleaned_data['title']
                desc= form.cleaned_data['desc']
                pst=Post(title=title, desc=desc)
                form.save()
                form=   PostForm()
        else:
            form=PostForm()
        img=Post.objects.all()
        context={'form':form,'img':img}
        return render(request,'blog/add.html',context)
    else:
        return HttpResponseRedirect('/login/')
    

def update(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        context={'form':form}
        return render(request,'blog/update.html',context)
    else:
        return HttpResponseRedirect('/login/')
    
def delete(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            pi.delete() 
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
    
    
def report(request):
    if request.method=='POST':
        form=ReportForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email= form.cleaned_data['email']
            username=form.cleaned_data['username']
            message=form.cleaned_data['message']
            pst=Report(name=name, email=email, username=username, message=message)
            form.save()
            form=ReportForm()
            return HttpResponseRedirect('/')
    else:
        form=ReportForm()
        context={'form':form}
        return render(request,'blog/report.html',context)
        