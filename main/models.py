from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

User = get_user_model()


class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f"{self.parent} -> {self.name}"
        return self.name


class Dish(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # gram = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    price = models.DecimalField(max_digits=10,
                                decimal_places=3)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title



class Comment(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='body')
    name = models.CharField(max_length=300)
    body = models.TextField(verbose_name='Описание')
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')

    def __str__(self):
        # return f"{self.name} --> {self.body}"
        return '%s - %s' % (self.dish.title, self.name)


