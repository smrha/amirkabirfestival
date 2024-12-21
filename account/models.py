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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    

class judgement(models.Model):
    referee = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='داور')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='رساله')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'داوری'
        verbose_name_plural = 'داوری ها'

    def __str__(self):
        return f"{ self.article.id } - { self.referee.username }"