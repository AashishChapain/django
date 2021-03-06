from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('detail_view', kwargs={'pk':self.pk})


class test_func(models.Model):
    test_name = models.CharField(max_length=100)
    test_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.test_name
