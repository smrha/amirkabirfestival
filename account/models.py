from django.db import models
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    class Status(models.TextChoices):
        UPLOADED = 'UPL'
        REVIEW = 'REV'
        ACCEPTED = 'ACC'
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_articles')
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=3,
                              choices=Status.choices,
                              default=Status.UPLOADED)
    education_group = models.CharField(max_length=64)
    teacher = models.CharField(max_length=120)
    teacher_mobile = models.CharField(max_length=11)
    teacher_email = models.CharField(max_length=120)
    adviser = models.CharField(max_length=120)
    adviser_mobile = models.CharField(max_length=11)
    adviser_email = models.CharField(max_length=120)
    defense_date = jmodels.jDateField(blank=True, null=True)
    article_score = models.IntegerField()
    # type = models.CharField(max_length=32)
    Requester = models.CharField(max_length=120)
    Requester_loc = models.CharField(max_length=120)
    summary = models.TextField()
    article_file = models.FileField(upload_to='articles/%Y/%m/%d/', default='articles/default.pdf')
    other = models.FileField(upload_to='articles/%Y/%m/%d/', default='articles/default.pdf')
    accept = models.FileField(upload_to='articles/%Y/%m/%d/', default='articles/default.pdf')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.title

class Education(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=120, blank=True)
    field_study = models.CharField(max_length=120, blank=True)
    degree = models.CharField(max_length=120)
    score = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=120)
    national_id = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=11)
    date_of_birth = jmodels.jDateField(blank=True, null=True)
    city_of_birth = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default='photos/default.png')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        
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

    def __str__(self):
        return self.title