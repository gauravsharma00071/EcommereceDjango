from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from .utils import TokenGenerator,generate_token
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.views.generic import View
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Paassword is not matching")
            return HttpResponse("password Incorrect")
            #return render(request,"signup.html")
        try:
            if User.objects.get(username=email):
                messages.info(request, "EMail Exist")
                return HttpResponse("Email Already Exist")
                #return render(request,'signup.html')
        except Exception as identifier:
            pass

        user = User.objects.create_user(email,email,password)
        user.is_active=False
        user.save()
        email_subject="Activate Your Account"
        message=render_to_string('activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
        })

        email_message= EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,{email},)
        email_message.send()
        messages.success(request,"Activate Your Account by clicking the link in your gmail")
        return redirect('/login')


        return HttpResponse("User Created")
    return render(request,"signup.html")

class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_encode(uidb64))
            user=User.objects.get(pk.uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user.token):
            user.is_active=True
            user.save()
            messages.info(request,"Account activated Successfully")
            return redirect('/login')
        return render(request,'activatefail.html')

def handlelogin(request):
    username=request.POST['email']
    userpassword=request.POST['pass1']
    myuser=authenticate(username=username,password=userpassword)

    if myuser is not None:
        login(request,myuser)
        messages.success(request,"Login Success")
        return redirect('/')
    else:
        messages.error(request,"Invalid Credentials")
        return redirect('login')

    return render(request,"login.html")

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/login')