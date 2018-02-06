# blog/models.py 

import datetime

from django.db import models
from django.urls import reverse 
from django.utils import timezone 

class Post(models.Model):

    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )

    title = models.CharField(max_length = 200)
    text = models.TextField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:home')
