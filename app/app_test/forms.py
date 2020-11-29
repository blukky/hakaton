from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import Tag, Post



#####################################################################################################################################

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Пост не может быть "Create"')
        return new_slug



class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug',]

        # применение стилей в форме. Результат будет <input class='form-control'>
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Тег не может быть "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Тег должен быть уникальным. Тег "{}" уже существует'.format(new_slug))
        return new_slug