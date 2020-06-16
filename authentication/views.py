from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseForbidden
from . forms import RegisterForm, LoginForm
from . models import Result
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login  as login_user, logout as logout_user
from django.contrib import messages

# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(username= form.cleaned_data.get('username'), 
            email = form.cleaned_data.get('email'))
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            messages.success(request,'Account is created successfully')
            return redirect('/login/')
    return render(request, 'register_form.html',{'form':form, 'title':'Register'})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username= form.cleaned_data.get('username'), 
            password = form.cleaned_data.get('password'))
            print(user)
            if user is not None:  
                login_user(request, user) 
                return render(request, 'quiz.html',{'title':'quiz'})
            else:
                return  render(request, 'login_form.html',{'form':form, 'title':'login','error':'Invalid credentials'})
    return  render(request, 'login_form.html',{'form':form, 'title':'login'})

def quiz(request, category):
    
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    try:
        res = Result.objects.get(user=request.user)
        if res:
            return render(request, 'exist.html',{'title':'quiz', 'result':res})
    except Result.DoesNotExist:
        res = None
        if res is None:
            return render(request, 'quiz_test.html',{'title':'quiz', 'category':category})
def logout(request):
    logout_user(request)
    return redirect('/login/')
def result(request):
    result = request.POST['result']
    current_user = request.user
    res = Result(user =current_user, result= result)
    res.save()
    if res.id:
        return HttpResponse(res.id)
    else:
        return HHttpResponse('something wrong')