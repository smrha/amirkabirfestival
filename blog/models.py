from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_jalali.db import models as jmodels
from extentions.utils import covert_to_jalali


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    class Category(models.TextChoices):
        DEFAULT = 'DF', 'پیش فرض'
        IMPORTANT = 'IM', 'اخبار مهم'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish',
                            allow_unicode=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    lead = models.TextField()
    body = RichTextField()
    views = models.PositiveIntegerField(default=0)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    category = models.CharField(max_length=2,
                              choices=Category.choices,
                              default=Category.DEFAULT)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
    
    # show jalali publish date string
    def j_publish(self):
        return covert_to_jalali(self.publish)

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.id,
                             self.slug])
