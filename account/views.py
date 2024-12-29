from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import LoginForm, UserEditForm, ProfileEditForm, CustomAuthenticationForm, \
    CustomUserCreationForm, EducationEditForm, ArticleForm, TicketForm, UploadToReviewForm, \
    ChoiceRefereeForm, ChoiceAssistantForm, REFEREES, QuizFirstForm, QuizSecondForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Education, Article, Judgement, Quiz
from django.contrib.auth.models import User
import csv
from io import BytesIO
from extentions.utils import send_sms

def export_to_excel(request):
    articles = Article.objects.all()
    f = BytesIO()
    responese = HttpResponse('text/csv')
    responese['Content-Disposition'] = 'attachment; filename=articles_export.csv'
    writer = csv.writer(responese,f, encoding='utf-8')
    writer.writerow(['user', 'title', 'education_group', 'teacher'])
    article_fileds = articles.values_list('user', 'title', 'education_group', 'teacher')
    for article in article_fileds:
        writer.writerow(article)
    return responese


class ArbitrationShowView(View):
    
    def get(self, request, id):
        article = Article.objects.get(id=id)
        if Quiz.objects.filter(article=article).filter(assistant=request.user).exists():
            return redirect('account:judge_list')
        if request.user.profile.education_group == Profile.EducationGroup.HUMANITIES:
            form = QuizSecondForm()
        else:
            form = QuizFirstForm()
        return render(request, 'account/arbitration.html', {'form': form})
    
    def post(self, request, id):
        article = Article.objects.get(id=id)
        if request.user.profile.education_group == Profile.EducationGroup.HUMANITIES:
            form = QuizSecondForm(request.POST)
        else:
            form = QuizFirstForm(request.POST)

        if form.is_valid:
            new_quiz = form.save(commit=False)
            new_quiz.article = article
            new_quiz.assistant = request.user
            new_quiz.save()
            return redirect('account:judge_list')
        return render(request, 'account/arbitration.html', {'form': form})

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

# A Class Based View for create and upload a new article
class ArticleCreateView(View):
    form_class = ArticleForm
    template_name = "account/article_create.html"

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.user = request.user
            new_article.save()
            messages.success(request, 'رساله شما با موفقیت ارسال شد.')
            return redirect('account:article_list')
        else:
            messages.error(request, 'خطا در ارسال رساله.')
        return render(request, self.template_name, {'form': form})



# A Class Based View for update an article
class ArticleUpdateView(View):

    def get(self, request, id):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        article = Article.objects.get(pk=id)
        form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
        return render(request, 'account/article_edit.html', {'form': form, 'article': article})
    
    def post(self, request, id):
        article = Article.objects.get(pk=id)
        form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'بروزرسانی رساله با موفقیت انجام شد.')
            return redirect("account:article_list")
        else:
            messages.error(request, ' خطا در بروزرسانی رساله.')
        return render(request, 'account/article_edit.html', {'form': form, 'article': article})
    

class ArticleListView(View):
    def get(self, request):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden()
        articles = Article.objects.all().filter(status=Article.Status.UPLOADED).order_by('-created')
        paginator = Paginator(articles, 10)
        page = request.GET.get('page', 1)
    
        try:
            result = paginator.page(page)
        except PageNotAnInteger:
            result = paginator.page(1)
        except EmptyPage:
            result = paginator.page(paginator.num_pages)
        
        return render(request, 'account/article_list.html', {'articles': result }) 

    

class ArticleShowView(View):
    upload_form = UploadToReviewForm    

    def get(self, request, id):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden()
        form = self.upload_form()
        article = Article.objects.get(id=id)
        # if article.status == Article.Status.values[0]:
        return render(request, 'account/article.html', {'article': article, 'form': form})
    
    def post(self, request, id):
        form = self.upload_form(request.POST)
        article = Article.objects.get(id=id)
        if form.is_valid():
            if form.cleaned_data["accept"] == True:
                article.status = Article.Status.REVIEW
                article.save()         
        return redirect('account:article_list')


class JudgementAssistantListView(View):

    def get(self, request):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden()
        articles = Article.objects.filter(judgements__referee=request.user).filter(status=Article.Status.EVALUATION).order_by('-created')
        paginator = Paginator(articles, 10)
        page = request.GET.get('page', 1)
    
        try:
            result = paginator.page(page)
        except PageNotAnInteger:
            result = paginator.page(1)
        except EmptyPage:
            result = paginator.page(paginator.num_pages)
        
        return render(request, 'account/assistant_list.html', {'articles': result })


class JudgementAssistantView(View):
    form_class = ChoiceAssistantForm

    def get(self, request, id):        
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden()
        article = Article.objects.get(id=id)
        referees = User.objects.filter(is_staff=True).filter(profile__education_group=request.user.profile.education_group)
        return render(request, 'account/assistant.html', {'article': article, 'referees': referees})
    
    def post(self, request, id):
        assists = request.POST.getlist('assistants')
        article = Article.objects.get(id=id)
        judgement = Judgement.objects.get(article=article)
        for item in assists:
            judgement.assistant.add(item)
            message = f"داور گرامی: رساله {article.title} جهت ارزیابی به کارتابل شما ارجاع شد. دبیرخانه جشنواره امیرکبیر"
            to = User.objects.get(id=item)
            mobile = to.username
            send_sms(message, mobile)
        article.status = Article.Status.ACCEPTED
        article.save()   
        return redirect('account:assistant_list')
    

class JudgementJudgeListView(View):
    def get(self, request):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden()
        articles = Article.objects.filter(judgements__assistant=request.user).filter(status=Article.Status.ACCEPTED).order_by('-created')
        paginator = Paginator(articles, 10)
        page = request.GET.get('page', 1)
    
        try:
            result = paginator.page(page)
        except PageNotAnInteger:
            result = paginator.page(1)
        except EmptyPage:
            result = paginator.page(paginator.num_pages)
        
        return render(request, 'account/judge_list.html', {'articles': result })


class JudgementJudgeView(View):

    def get(self, request, id):        
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden()
        article = Article.objects.get(id=id)
        flag = Quiz.objects.filter(article=article).filter(assistant=request.user).exists()
        judge = request.user.assistant_judgements.get(article__id=id)
        return render(request, 'account/judge.html', {'article': article, 'judge': judge, 'flag':flag})
    

class JudgementListView(View):

    def get(self, request):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden()
        if request.user.profile.type == Profile.Type.REFEREE:
            # articles = Article.objects.all().filter(status=Article.Status.REVIEW).filter(judgements=request.user.judgements).order_by('-created')
            articles =Article.objects.filter(judgements__referee=request.user).filter(status=Article.Status.REVIEW).order_by('-created')
        else:
            articles =Article.objects.filter(status=Article.Status.REVIEW).order_by('-created')
        paginator = Paginator(articles, 10)
        page = request.GET.get('page', 1)
    
        try:
            result = paginator.page(page)
        except PageNotAnInteger:
            result = paginator.page(1)
        except EmptyPage:
            result = paginator.page(paginator.num_pages)
        
        return render(request, 'account/judgement_list.html', {'articles': result }) 


class JudgementRefereeView(View):
    form_class = ChoiceRefereeForm

    def get(self, request, id):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden()
        form = self.form_class()
        article = Article.objects.get(id=id)
        return render(request, 'account/referee.html', {'article': article, 'form': form})
    
    def post(self, request, id):
        form = self.form_class(request.POST)
        article = Article.objects.get(id=id)
        if form.is_valid():
            referee_id =int(form.cleaned_data["referee"])
            Judgement.objects.create(referee_id=referee_id, article=article)
            article.status = Article.Status.EVALUATION
            article.save()
        return redirect('account:judgement_list')


# Show list of user articles
class UserArticleListView(View):
    def get(self, request):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden()
        articles = Article.objects.filter(user=request.user)
        return render(request, 'account/user_article_list.html', {'articles': articles}) 

# Add a ticket view
def ticket_add(request):
    if not request.user.is_authenticated:
            return HttpResponseForbidden()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.creator = request.user
            new_ticket.save()
            messages.success(request, 'تیکت ارسال شد.')
        else:
            messages.error(request, 'خطا در ارسال تیکت')
    else:
        form = TicketForm()
    return render(request, 'account/ticket_add.html', {'form': form}) 



# User education profile edit view
def education_edit(request):
    if not request.user.is_authenticated:
            return HttpResponseForbidden()
    if request.method == 'POST':
        form = EducationEditForm(instance=request.user.education, 
                                 data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'بروزرسانی انجام شد.')
        else:
            messages.error(request, 'خطا در بروزرسانی')
    else:
        form = EducationEditForm(instance=request.user.education)
    return render(request, 'account/education_edit.html', {'form': form})

# User profile edit view
def profile_edit(request):
    if not request.user.is_authenticated:
            return HttpResponseForbidden()
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, 
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, 
                                       data=request.POST, 
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'بروزرسانی انجام شد.')
        else:
            messages.error(request, 'خطا در بروزرسانی')
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
                return redirect("account:dashboard")
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

class DashboardView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return render(request, 'account/home.html')
        

def home(request):
    return render(request, 'account/home.html')

def user_logout(request):
    logout(request)
    return redirect('main')



