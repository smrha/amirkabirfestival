from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('account:user_profile',
            args=[self.id])