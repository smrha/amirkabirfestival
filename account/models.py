from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_articles')
    title = models.CharField(max_length=255)
    education_group = models.CharField(max_length=64)
    teacher = models.CharField(max_length=120)
    teacher_mobile = models.CharField(max_length=11)
    teacher_email = models.CharField(max_length=120)
    adviser = models.CharField(max_length=120)
    adviser_mobile = models.CharField(max_length=11)
    adviser_email = models.CharField(max_length=120)
    # defense_date = models.DateField()
    article_score = models.IntegerField()
    type = models.CharField(max_length=32)
    Requester = models.CharField(max_length=120)
    Requester_loc = models.CharField(max_length=120)
    # confirmation = models.CharField(max_length=120)
    summary = models.TextField()
    # file
    # other
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
    date_of_birth = models.DateField(blank=True, null=True)
    city_of_birth = models.CharField(max_length=120)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.user.first_name

    # def get_absolute_url(self):
    #     return reverse('account:user_profile', args=[self.id])