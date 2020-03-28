from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'items'



class Info(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='pics',blank=True)
    address = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    DOB = models.DateField()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Profiles'