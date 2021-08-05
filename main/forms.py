from django import forms

from .models import *


class CreateDishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"


class UpdateDishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"


class ReviewAddForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['body', 'user']