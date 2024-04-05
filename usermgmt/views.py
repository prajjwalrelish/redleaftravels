from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model,login,logout
from django.contrib import messages
from home.tasks import email_send
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string


# Create your views here.
def user_logout(request):
    logout(request)
    # messages.success(request,'Successfully logged out')
    return redirect('home')
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        # authenticate the user
        user = authenticate(request,username=username,password=password)

        if user is not None:
            if not user.is_active :
                messages.error(request,"Your account is not active, please confirm your email to activate your account ")   
                return render(request, "login.html")
            else:
                login(request,user)
                return redirect('home')
        else: 
            messages.error(request,"Couldn't login check your username or password again")
    
    return render(request, "login.html")

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1= request.POST.get('password1')
        pass2= request.POST.get('password2')

        email_match = User.objects.filter(email = email)
        username_match = User.objects.filter(username = username)
        if username_match : 
            messages.error(request,f'the username "{username}" already exists ')
            
        elif email_match :
            messages.error(request,f"the email '{email}' already exists")
            
        elif pass1 != pass2 :
            messages.error(request,"passwords didn't match")
            
        else: 
            myuser = User.objects.create_user(username,email ,pass1) 
            myuser.is_active = False # default false until email is verified
            myuser.save()

            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('email_confirm/acc_active_email.html', {  
                    'user': myuser,  
                    'domain': current_site.domain,  
                    'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),  
                    'token':default_token_generator.make_token(myuser),  
                }) 
            # send email using celery function
            email_send.delay(mail_subject,message,email)
            return render(request,'email_confirm/email_send.html')
      

    return render(request, "signup.html")


# to activate the email ( user email confirmation ) 
def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and default_token_generator.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return render(request,'email_confirm/email_confirm.html')
    else:  
        return  render(request,'email_confirm/invalid_link.html')