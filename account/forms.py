from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django_jalali import forms as jforms
from django_jalali.admin.widgets import AdminjDateWidget
from django import forms
from .models import Profile, Education, Article

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


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label="عنوان رساله / پایان نامه",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    education_group = forms.CharField(
        label="گروه آموزشی",
        widget=forms.Select(choices=GROUP_CHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    teacher = forms.CharField(
        label="نام استاد راهنما",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    teacher_mobile = forms.CharField(
        label="موبایل استاد راهنما",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    teacher_email = forms.CharField(
        label="ایمیل استاد راهنما",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    adviser = forms.CharField(
        label="نام استاد مشاور",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    adviser_mobile = forms.CharField(
        label="موبایل استاد مشاور",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    adviser_email = forms.CharField(
        label="ایمیل استاد مشاور",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    article_score = forms.IntegerField(
        label="نمره رساله",
        widget=forms.NumberInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    type = forms.CharField(
        label="نوع رساله",
        widget=forms.Select(choices=TYPE_CHOICES,
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    summary = forms.CharField(
        label="چکیده  رساله / پایان نامه",
        widget=forms.Textarea(
            attrs={"class": "block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    Requester = forms.CharField(
        label="تقاضا دهنده",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    Requester_loc = forms.CharField(
        label="آدرس تقاضا دهنده",
        widget=forms.TextInput(
            attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        )
    article_file = forms.FileField(
        label="فایل رساله",
        widget=forms.FileInput(
            attrs={"class": "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"})
        )
    other = forms.FileField(
        label="دیگر فایل ها",
        widget=forms.FileInput(
            attrs={"class": "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"})
        )
    accept = forms.FileField(
        label="تأییدیه حسن انجام کار یا گواهی کارفرما",
        widget=forms.FileInput(
            attrs={"class": "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"})
        )
    
    class Meta:
        model = Article
        fields = ['title', 'education_group', 'teacher', 'teacher_mobile', 'teacher_email',
                  'adviser', 'adviser_mobile', 'adviser_email', 'article_score', 'type', 'accept',
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
    score = forms.IntegerField(
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
    
