from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django_jalali import forms as jforms
from django_jalali.admin.widgets import AdminjDateWidget
from django import forms
from .models import Profile, Education, Article, Ticket, Quiz

from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class JdateInput(AdminjDateWidget):
    input_type = 'date'

GROUP_CHOICES = (
    ('فنی و مهندسی', 'فنی و مهندسی'),
    ('علوم انسانی', 'علوم انسانی'),
    ('علوم پایه', 'علوم پایه'),
    ('علوم پزشکی', 'علوم پزشکی'),
    ('دامپزشکی و علوم دامی', 'دامپزشکی و علوم دامی'),
    ('هنر و معماری', 'هنر و معماری'),
    ('کشاورزی، منابع طبیعی و محیط زیست', 'کشاورزی، منابع طبیعی و محیط زیست'),
)

TYPE_CHOICES = (
    ('کاربردی', 'کاربردی'),
    ('کارفرمایی', 'کارفرمایی'),
)

REFEREES =( 
    ("291", "علی قنبری - فنی و مهندسی"),
    ("292", "نادر شکراللهی - علوم انسانی"),
    ("293", "احمد زنگانه - علوم انسانی"),
    ("294", "کامبیز پورطهماسی - کشاورزی…"),
    ("295", "عزیزالله حبیبی - علوم پایه"),
    ("296", "راضیه لطفی - علوم پزشکی"), 
    ("297", "سهیلا مرادی - دامپزشکی و علوم دامی"), 
    ("298", "سارا دشتگرد - هنر و معماری"), 
) 


class UploadToReviewForm(forms.Form):
    accept = forms.BooleanField(
        label="این رساله مورد تایید بوده و جهت بررسی به دبیر جشنواره ارسال می گردد.",
        widget=forms.CheckboxInput(
            attrs={"class": "w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"})
        )


class ChoiceRefereeForm(forms.Form):
    referee = forms.CharField(
        label='',
        widget=forms.Select(
            choices=REFEREES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
    )


class ChoiceAssistantForm(forms.Form):
    assistant = forms.MultipleChoiceField()
    #     widget=forms.Select(
    #         choices=REFEREES,
    #         attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
    # ) 


class TicketForm(forms.ModelForm):
    title = forms.CharField(
        label="عنوان",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    description = forms.CharField(
        label="توضیحات",
        widget=forms.Textarea(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    
    class Meta:
        model = Ticket
        fields = ['title', 'description']

class ArticleForm(forms.ModelForm):
    required_error_message = "فیلد الزامی می باشد"
    title = forms.CharField(
        error_messages={"required": required_error_message},
        label="عنوان رساله / پایان نامه",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    education_group = forms.CharField(
        error_messages={"required": required_error_message},
        label="گروه آموزشی",
        widget=forms.Select(choices=GROUP_CHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    teacher = forms.CharField(
        error_messages={"required": required_error_message},
        label="نام استاد راهنما",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    teacher_mobile = forms.CharField(
        error_messages={"required": required_error_message},
        label="موبایل استاد راهنما",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    teacher_email = forms.CharField(
        error_messages={"required": required_error_message},
        label="ایمیل استاد راهنما",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    adviser = forms.CharField(
        error_messages={"required": required_error_message},
        label="نام استاد مشاور",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    adviser_mobile = forms.CharField(
        error_messages={"required": required_error_message},
        label="موبایل استاد مشاور",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    adviser_email = forms.CharField(
        error_messages={"required": required_error_message},
        label="ایمیل استاد مشاور",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    article_score = forms.FloatField(
        error_messages={"required": required_error_message},
        label="نمره رساله / پایان نامه",
        widget=forms.NumberInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    summary = forms.CharField(
        error_messages={"required": required_error_message},
        label="چکیده  رساله / پایان نامه",
        widget=forms.Textarea(
            attrs={"class": "block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    Requester = forms.CharField(
        error_messages={"required": required_error_message},
        label="تقاضا دهنده",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    Requester_loc = forms.CharField(
        error_messages={"required": required_error_message},
        label="آدرس تقاضا دهنده",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    article_file = forms.FileField(
        error_messages={"required": required_error_message},
        label="فایل رساله / پایان نامه",
        widget=forms.FileInput(
            attrs={"class": "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"})
        )
    other = forms.FileField(
        error_messages={"required": required_error_message},
        label="دیگر فایل ها",
        widget=forms.FileInput(
            attrs={"class": "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"})
        )
    accept = forms.FileField(
        error_messages={"required": required_error_message},
        label="تأییدیه حسن انجام کار یا گواهی کارفرما",
        widget=forms.FileInput(
            attrs={"class": "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"})
        )
    
    class Meta:
        model = Article
        fields = ['title', 'education_group', 'teacher', 'teacher_mobile', 'teacher_email',
                  'adviser', 'adviser_mobile', 'adviser_email', 'article_score', 'accept',
                  'summary', 'Requester', 'Requester_loc', 'article_file', 'defense_date', 'other']
    
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['defense_date']=JalaliDateField(label=('تاریخ دفاع'),
                                              widget=AdminJalaliDateWidget)



class EducationEditForm(forms.ModelForm):
    university = forms.CharField(
        label="دانشگاه محل تحصیل",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    field_study = forms.CharField(
        label="رشته تحصیلی",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    degree = forms.CharField(
        label="مدرک تحصیلی",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    score = forms.FloatField(
        label="معدل",
        widget=forms.NumberInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    
    class Meta:
        model = Education
        fields = ['university', 'field_study', 'degree', 'score']
    

class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(
        label="نام",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    last_name = forms.CharField(
        label="نام خانوادگی",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    email = forms.CharField(
        label="ایمیل",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    father_name = forms.CharField(
        label="نام پدر",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    national_id = forms.CharField(
        label="کد ملی",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"})
    )
    mobile_number = forms.CharField(
        label="موبایل",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"})
    )
    # date_of_birth = JalaliDateField(
    #     label="تاریخ تولد",
    #     widget=AdminDateWidget(
    #         attrs={"class": ""})
    # )
    city_of_birth = forms.CharField(
        label="محل تولد",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"})
    )
    photo = forms.ImageField(
        label='عکس',
        widget=forms.FileInput(
            attrs={"class": "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"})            
    )

    class Meta:
        model = Profile
        fields = ['father_name', 'national_id', 'mobile_number', 'date_of_birth', 'city_of_birth', 'photo']

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth']=JalaliDateField(label=('تاریخ تولد'),
                                              widget=AdminJalaliDateWidget)

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    password1 = forms.CharField(
        label="رمز ورود",
        widget=forms.PasswordInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    password2 = forms.CharField(
        label="تکرار رمز ورود",
        widget=forms.PasswordInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    password = forms.CharField(
        label="رمز ورود",
        widget=forms.PasswordInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    

class ProfileForm(forms.ModelForm):
    father_name = forms.CharField(
        label="نام پدر",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"})
        )
    national_id = forms.CharField(
        label="کد ملی",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"})
    )
    mobile_number = forms.CharField(
        label="موبایل",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"})
    )
    date_of_birth = forms.DateField(
        label="تاریخ تولد",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"})
    )
    city_of_birth = forms.CharField(
        label="محل تولد",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"})
    )

    class Meta:
        model = Profile
        fields = ['father_name', 'national_id', 'mobile_number', 'date_of_birth', 'city_of_birth']
        # widgets = {
        # 'url': forms.HiddenInput,
        # }


class LoginForm(forms.Form):
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )


VALUESCHOICES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

class QuizFirstForm(forms.ModelForm):
    quest_1 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در رفع یک مشکل یا مسئله (اجتماعی، اقتصادی، فنی، محیط زیستی، آموزشی)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_2 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در شناسایی راهکارهای مدیریتی',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_3 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در ساده تر شدن نظام تصمیم گیری',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_4 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در دقیق تر شدن نظام تصمیم گیری',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_5 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش هماهنگی و یکپارچگی سیستم تصمیم گیری (ارتقأ سازماندهی)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_6 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در تسهیل دسترسی به داده و اطلاعات',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_7 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در حمایت از تصمیم گیری مشارکتی',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_8 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش بهره وری سیستم (سازمان اداری، بنگاه تولیدی یا خدماتی، یا هر  برنامه)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_9 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش کارآیی منابع مالی (کاهش هزینه ها)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_10 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش کارآیی نیروی انسانی ',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_11 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش کارآیی تجهیزات و سخت افزارها و ارتقأ فناوری',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_12 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش کارآیی اطلاعات و نرم افزارها',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_13 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش کارآیی منابع طبیعی (خاک، آب، گیاه)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_14 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش تاب آوری سیستم (سازمان اداری، بنگاه تولیدی یا خدماتی، یا هر  برنامه)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_15 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در بهبود کمیت تولید',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_16 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در بهبود کیفیت تولید',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_17 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در حمایت بیشتر از تنوع زیستی و سیستم های حیات بخش (اکوسیستم ها)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_18 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در کاهش مصرف انرژی های فسیلی',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_19 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در استفاده از منابع انرژی تجدید پذیر و پاک',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_20 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در کاهش آلودگی محیط زیست',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_21 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در ارتقأ سلامت اکوسیستم و حفظ منابع طبیعی',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_22 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در ارتقأ امنیت آب (بازیافت آب، ردپای آب، دیپلماسی آب)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_23 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در بهبود کیفیت زندگی و سلامت انسان',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_24 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش ایمنی زندگی و فعالیت انسان (در مقابل مخاطرات طبیعی)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_25 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش امنیت زندگی و فعالیت (پدافند غیرعامل)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_26 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در ارتقأ امنیت غذایی',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_27 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در کارآفرینی (شناسایی و بهره برداری از فرصت ها)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_28 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در رونق کسب و کار و تنوع بخشیدن به آن',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_29 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در ارتقأ رضایت مشتری های سیستم',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_30 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش خلاقیت ',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_31 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش نوآوری ',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_32 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در تقویت مسئولیت پذیری اجتماعی (اعتماد، انسجام، تقویت، پاسخگویی، اخلاق محیط زیست و حقوق منابع)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    
    class Meta:
        model= Quiz
        fields = ['quest_1', 'quest_2', 'quest_3', 'quest_4', 'quest_5', 
                  'quest_6', 'quest_7', 'quest_8', 'quest_9', 'quest_10',
                  'quest_11', 'quest_12', 'quest_13', 'quest_14', 'quest_15',
                  'quest_16', 'quest_17', 'quest_18', 'quest_19', 'quest_20',
                  'quest_21', 'quest_22', 'quest_23', 'quest_24', 'quest_25', 
                  'quest_26', 'quest_27', 'quest_28', 'quest_29', 'quest_30',
                  'quest_31', 'quest_32',]


class QuizSecondForm(forms.ModelForm):
    quest_1 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در رفع یک مشکل یا مسئله (اجتماعی، اقتصادی، فنی، محیط زیستی، آموزشی)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_2 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در شناسایی راهکارهای مدیریتی',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_3 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در ساده تر شدن نظام تصمیم¬گیری',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_4 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در دقیق تر شدن نظام تصمیم¬گیری',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_5 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش هماهنگی و یکپارچگی سیستم تصمیم¬گیری (ارتقأ سازماندهی)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_6 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در تسهیل دسترسی به داده و اطلاعات',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_7 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در حمایت از تصمیم¬گیری مشارکتی',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_8 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش بهره وری سیستم (سازمان اداری، بنگاه تولیدی یا خدماتی، یا هر  برنامه)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_9 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش کارآیی منابع مالی (کاهش هزینه ها)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_10 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش کارآیی نیروی انسانی ',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_11 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش کارآیی تجهیزات و سخت افزارها و ارتقأ فناوری',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_12 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش کارآیی اطلاعات و نرم افزارها',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_13 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش کارآیی منابع ارزش آفرین (انسانی، اقتصادی، اجتماعی فرهنگی، استراتژیک)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_14 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش تاب¬آوری سیستم (سازمان اداری، بنگاه تولیدی یا خدماتی و ... )',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_15 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در استفاده از منابع انرژی تجدید پذیر و پاک',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_16 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در کاهش آلودگی محیط زیست',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_17 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در ارتقأ فرهنگ حفظ منابع طبیعی',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_18 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در بهبود کیفیت زندگی و بهداشت روانی',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_19 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش امنیت زندگی و فعالیت¬های فرهنگی و اجتماعی(پدافند غیرعامل)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_20 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در ارتقأ امنیت اجتماعی',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_21 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در ارتقأ امنیت اقتصادی',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_22 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در ارتقأ امنیت سیاسی',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_23 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در کارآفرینی (شناسایی و بهره برداری از فرصت¬ها)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_24 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در رونق کسب و کار و تنوع بخشیدن به آن',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_25 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در ارتقأ رضایت مشتری¬های سیستم',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_26 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش خلاقیت ',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_27 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در افزایش نوآوری ',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    quest_28 = forms.IntegerField(
        label='توفیق دستاورد پژوهش در تقویت مسئولیت پذیری اجتماعی (اعتماد، انسجام، تقویت، پاسخگویی، اخلاق محیط زیست و حقوق منابع)',
        widget=forms.Select(
            choices=VALUESCHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"})
        )
    
    class Meta:
        model= Quiz
        fields = ['quest_1', 'quest_2', 'quest_3', 'quest_4', 'quest_5', 
                  'quest_6', 'quest_7', 'quest_8', 'quest_9', 'quest_10',
                  'quest_11', 'quest_12', 'quest_13', 'quest_14', 'quest_15',
                  'quest_16', 'quest_17', 'quest_18', 'quest_19', 'quest_20',
                  'quest_21', 'quest_22', 'quest_23', 'quest_24', 'quest_25', 
                  'quest_26', 'quest_27', 'quest_28']

