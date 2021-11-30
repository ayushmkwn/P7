from django.shortcuts import render,HttpResponse
from .forms import RegisterForm,ProfileForm
from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import addPost
from django.contrib.auth.models import User
from .models import Post,UserProfile
from django.conf import settings
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .token import account_activation_token
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from .decorators import allowed_users
from django.contrib.auth.models import Group


def registerUser(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            Msub = 'Activate your account on Social Media Site'
            msg = render_to_string('registration/acc_active_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                    })
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,]
            send_mail(Msub, msg, email_from, recipient_list)
            return HttpResponse("Please confirm your email address to complete the registration!")
        else:
            context={'form':form}
            messages.error(request,'There is Error in your information...kindly refill the form')
            render(request,'registration/signup.html',context)
    form=RegisterForm()
    context={'form':form}
    return render(request,'registration/signup.html',context)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        group = Group.objects.get(name='customer')
        user.groups.add(group)
        user.save()
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        messages.success(request, 'Please complete your profile in profile section after login.')
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')

@allowed_users(allowed_roles=['admin'])
def add_post(request):
    pi = User.objects.get(username=request.user)
    if(request.method == 'POST'):
        fm = addPost(request.POST)
        if(fm.is_valid()):
            pname = fm.cleaned_data['postname']
            desc = fm.cleaned_data['description']
            reg = Post(postusername=pi, postname=pname, description=desc)
            reg.save()
            fm = addPost()
    else:
        fm = addPost()
    return render(request, 'registration/addPost.html', {'form':fm})

@allowed_users(allowed_roles=['admin'])
def show_post(request):
    stud = Post.objects.filter(postusername=request.user)
    return render(request, 'registration/showPost.html' , {'stu':stud})

@allowed_users(allowed_roles=['admin'])
def delete_post(request,postname):
    if request.method == 'POST':
        pi = Post.objects.get(postusername=request.user,postname=postname)
        pi.delete()
        stud = Post.objects.filter(postusername=request.user)
    return render(request, 'registration/showPost.html' , {'stu':stud})

@allowed_users(allowed_roles=['admin'])
def update_post(request, id):
    if request.method == 'POST':
        pi = Post.objects.get(pk=id,postusername=request.user)
        fm = addPost(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Post.objects.get(pk=id,postusername=request.user)
        fm = addPost(instance=pi)
    return render(request, 'registration/updatePost.html', {'form':fm})

def view_profile(request):
    if not UserProfile.objects.filter(username=request.user).exists(): 
        if request.method=="POST":
            fm=ProfileForm(request.POST,request.FILES)
            if fm.is_valid():
                uname = request.user
                email = uname.email
                bdate = fm.cleaned_data['birthdate']
                mobno = fm.cleaned_data['mobileno']
                gender = fm.cleaned_data['gender']
                city = fm.cleaned_data['city']
                pincode = fm.cleaned_data['pincode']
                profile = fm.cleaned_data['profile']
                document = fm.cleaned_data['document']
                reg = UserProfile(username=uname, email=email,birthdate=bdate,mobileno=mobno, gender=gender,city=city,pincode=pincode,profile=profile,document=document)
                reg.save()
                fm = ProfileForm()
                return redirect('user_profile')
            else:
                context={'form':fm}
                messages.error(request,'There is Error in your information...kindly refill the form')
                render(request,'registration/userProfile.html',context)            
        fm=ProfileForm()
        return render(request, 'registration/userProfile.html', {'form':fm})
    
    stud = UserProfile.objects.filter(username=request.user)
    return render(request, 'registration/showProfile.html' , {'stu':stud})

# @allowed_users(allowed_roles=['admin'])
def home(request):
    return render(request,'home.html')
