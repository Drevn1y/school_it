from datetime import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=128)
    count = models.IntegerField()
    des = models.TextField(max_length=512)
    photo = models.ImageField(upload_to='media')
    price = models.FloatField()
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




