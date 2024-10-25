from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserEditForm, ProfileEditForm, CustomAuthenticationForm, \
    CustomUserCreationForm, EducationEditForm, ArticleForm
from .models import Profile, Education
from blog.models import Post


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

def main(request):
    posts = Post.published.all()
    return render(request, 'blog/main.html', {'posts': posts})

def article_add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.user = request.user
            new_article.save()
    else:
        form = ArticleForm()
    return render(request, 'account/article_add.html', {'form': form})

def education_edit(request):
    if request.method == 'POST':
        form = EducationEditForm(instance=request.user.education, 
                                 data=request.POST)
        if form.is_valid():
            print("valid")
            form.save()
    else:
        form = EducationEditForm(instance=request.user.education)
    return render(request, 'account/education_edit.html', {'form': form})

def profile_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, 
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, 
                                       data=request.POST, 
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html', 
                  {'user_form': user_form, 
                   'profile_form': profile_form})

def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            Education.objects.create(user=new_user)

            return redirect('account:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("account:home")
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def home(request):
    return render(request, 'account/home.html')

def user_logout(request):
    logout(request)
    return redirect('main')



