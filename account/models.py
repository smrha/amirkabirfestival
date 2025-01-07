from django.db import models
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    class Status(models.TextChoices):
        UPLOADED = 'UPL'
        REVIEW = 'REV'
        EVALUATION = 'EVA'
        ACCEPTED = 'ACC'
        
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_articles', verbose_name='کاربر')
    title = models.CharField(max_length=255, verbose_name='عنوان رساله')
    status = models.CharField(max_length=3,
                              choices=Status.choices,
                              default=Status.UPLOADED, verbose_name='وضعیت')
    education_group = models.CharField(max_length=64, verbose_name='گروه آموزشی')
    teacher = models.CharField(max_length=120, verbose_name='استاد')
    teacher_mobile = models.CharField(max_length=11, verbose_name='موبایل استاد')
    teacher_email = models.CharField(max_length=120, verbose_name='ایمیل استاد')
    adviser = models.CharField(max_length=120, verbose_name='راهنما')
    adviser_mobile = models.CharField(max_length=11, verbose_name='موبایل راهنما')
    adviser_email = models.CharField(max_length=120, verbose_name='ایمیل راهنما')
    defense_date = jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ دفاع')
    article_score = models.FloatField(verbose_name='نمره مقاله')
    Requester = models.CharField(max_length=120, verbose_name='درخواست دهنده')
    Requester_loc = models.CharField(max_length=120, verbose_name='آدرس درخواست دهنده')
    summary = models.TextField(verbose_name='چکیده')
    article_file = models.FileField(upload_to='articles/%Y/%m/%d/', default='articles/default.pdf', verbose_name='فایل مقاله')
    other = models.FileField(upload_to='articles/%Y/%m/%d/', default='articles/default.pdf', verbose_name='دیگر')
    accept = models.FileField(upload_to='articles/%Y/%m/%d/', default='articles/default.pdf', verbose_name='تاییدیه')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'رساله'
        verbose_name_plural = ' رساله ها'
        
    def __str__(self):
        return self.title

class Education(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    university = models.CharField(max_length=120, blank=True, verbose_name='دانشگاه')
    field_study = models.CharField(max_length=120, blank=True, verbose_name='رشته تحصیلی')
    degree = models.CharField(max_length=120, verbose_name='مقطع تحصیلی')
    score = models.FloatField(default=0, verbose_name='معدل')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'سابقه تحصیلی'
        verbose_name_plural = 'سوابق تحصیلی'
        
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Profile(models.Model):
    class Type(models.TextChoices):
        PARTICIPANT = 'شرکت کننده'
        CHIEF = 'سرداور'
        REFEREE = 'داور'

    class EducationGroup(models.TextChoices):
        ART = 'هنر و معماری'
        HUMANITIES = 'علوم انسانی'
        ENGINEERING = 'فنی و مهندسی'
        SCIENCE = 'علوم پایه'
        AGRICULTURAL = 'کشاورزی، منابع طبیعی و محیط زیست'
        MEDICAL = 'علوم پزشکی'
        VETERINARY = 'دامپزشکی و علوم دامی'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=32,
                              choices=Type.choices,
                              default=Type.PARTICIPANT, verbose_name='نوع حساب کاربری')
    education_group = models.CharField(max_length=32,
                                       choices=EducationGroup.choices,
                                       default=EducationGroup.ENGINEERING)
    father_name = models.CharField(max_length=120, verbose_name='نام پدر')
    national_id = models.CharField(max_length=10, verbose_name='کد ملی')
    mobile_number = models.CharField(max_length=11, verbose_name='موبایل')
    date_of_birth = jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ تولد')
    city_of_birth = models.CharField(max_length=120, verbose_name='محل تولد')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default='photos/default.png', verbose_name='عکس')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفابل کاربران'
        
    def __str__(self):
        return self.user.first_name

    # def get_absolute_url(self):
    #     return reverse('account:user_profile', args=[self.id])


class Ticket(models.Model):
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'

    def __str__(self):
        return self.title
    

class Judgement(models.Model):
    referee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='judgements', verbose_name='سر داور')
    assistant = models.ManyToManyField(User, 
                                       related_name='assistant_judgements', 
                                       blank=True, 
                                       null=True, 
                                       verbose_name='داوران')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='judgements', verbose_name='رساله')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'داوری'
        verbose_name_plural = 'داوری ها'

    def __str__(self):
        return f"{ self.article.id } - { self.referee.username }"
    

class Quiz(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    assistant = models.ForeignKey(User, on_delete=models.CASCADE)
    quest_1 = models.PositiveIntegerField(blank=True, default=0)
    quest_2 = models.PositiveIntegerField(blank=True, default=0)
    quest_3 = models.PositiveIntegerField(blank=True, default=0)
    quest_4 = models.PositiveIntegerField(blank=True, default=0)
    quest_5 = models.PositiveIntegerField(blank=True, default=0)
    quest_6 = models.PositiveIntegerField(blank=True, default=0)
    quest_7 = models.PositiveIntegerField(blank=True, default=0)
    quest_8 = models.PositiveIntegerField(blank=True, default=0)
    quest_9 = models.PositiveIntegerField(blank=True, default=0)
    quest_10 = models.PositiveIntegerField(blank=True, default=0)
    quest_11 = models.PositiveIntegerField(blank=True, default=0)
    quest_12 = models.PositiveIntegerField(blank=True, default=0)
    quest_13 = models.PositiveIntegerField(blank=True, default=0)
    quest_14 = models.PositiveIntegerField(blank=True, default=0)
    quest_15 = models.PositiveIntegerField(blank=True, default=0)
    quest_16 = models.PositiveIntegerField(blank=True, default=0)
    quest_17 = models.PositiveIntegerField(blank=True, default=0)
    quest_18 = models.PositiveIntegerField(blank=True, default=0)
    quest_19 = models.PositiveIntegerField(blank=True, default=0)
    quest_20 = models.PositiveIntegerField(blank=True, default=0)
    quest_21 = models.PositiveIntegerField(blank=True, default=0)
    quest_22 = models.PositiveIntegerField(blank=True, default=0)
    quest_23 = models.PositiveIntegerField(blank=True, default=0)
    quest_24 = models.PositiveIntegerField(blank=True, default=0)
    quest_25 = models.PositiveIntegerField(blank=True, default=0)
    quest_26 = models.PositiveIntegerField(blank=True, default=0)
    quest_27 = models.PositiveIntegerField(blank=True, default=0)
    quest_28 = models.PositiveIntegerField(blank=True, default=0)
    quest_29 = models.PositiveIntegerField(blank=True, default=0)
    quest_30 = models.PositiveIntegerField(blank=True, default=0)
    quest_31 = models.PositiveIntegerField(blank=True, default=0)
    quest_32 = models.PositiveIntegerField(blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'پرسشنامه'
        verbose_name_plural = 'پرسشنامه ها'

    def __str__(self):
        return f"{self.article.title}-{self.assistant.first_name} {self.assistant.last_name}"
    
    def result(self):
        result = self.quest_1 +  self.quest_2 +  self.quest_3 +  self.quest_4 + self.quest_5 + self.quest_6 +  self.quest_7 +  self.quest_8 +  self.quest_9 + self.quest_10 + self.quest_11 +  self.quest_12 +  self.quest_13 +  self.quest_14 + self.quest_15 + self.quest_16 +  self.quest_17 +  self.quest_18 +  self.quest_19 + self.quest_20 + self.quest_21 +  self.quest_22 +  self.quest_23 +  self.quest_24 + self.quest_25 + self.quest_26 +  self.quest_27 +  self.quest_28 +  self.quest_29 + self.quest_30 + self.quest_31 + self.quest_32      
        return result


# class Question(models.Model):
#     title = models.CharField(max_length=255, verbose_name='سوال')
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['-created']
#         verbose_name = 'سوال'
#         verbose_name_plural = 'سوالات'

#     def __str__(self):
#         return self.title
    

# class Response(models.Model):
#     assistant = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='سوال')
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='رساله')
#     value = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='پاسخ')
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['-created']
#         verbose_name = 'پاسخ'
#         verbose_name_plural = 'پاسخنامه'

#     def __str__(self):
#         return self.question.id