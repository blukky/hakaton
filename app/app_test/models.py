from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

from django.views import View

    
#####################################################################################################################################


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

#####################################################################################################################################
#############################################                   МОДЕЛЬ ПОСТОВ              ##########################################
#####################################################################################################################################

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True) # заголовок отзыва
    slug = models.SlugField(max_length=150, blank=True, unique=True) # уникальность
    body = models.TextField(blank=True,db_index=True) # тело отзыва
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts') # связанные теги
    date_pub = models.DateTimeField(auto_now_add=True) # дата публикации

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # для ссылок
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title

#####################################################################################################################################
#############################################                   МОДЕЛЬ ТЕГОВ              ###########################################
#####################################################################################################################################

class Tag(models.Model):
    title = models.CharField(max_length=50) # заголовок тега
    slug = models.SlugField(max_length=50, unique=True)  # уникальность

    def  get_absolute_url(self):
        # для ссылок
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)
    